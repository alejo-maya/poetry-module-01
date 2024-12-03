from typing import Optional, cast

from common.util.resources_list import ResourcesList
from common.util.azure_locations import AzureLocations


class NameGenerator:
    """
    This class allows to define environment and location of the resources and get the abbreviation of them

    Attributes
    ----------
    environments : object
        List of environments where we want to create the resource (dev,sandbox,prod,...)
    locations : object
        List of locations where we want to create the resource (eastus,westus2,...)
    resources : object
        List of resources in Azure with its properties (abbr,alphanum,global,dash_allowed)
    """

    prefix: str | None = None
    workload: str
    location: str
    env: str

    spokes = {
        "admin": "ad",
        "build": "bd",
        "hub": "hb",
    }

    environments = {
        "admin": "ad",
        "alpha": "ap",
        "beta": "bt",
        "build": "bd",
        "carry": "cy",
        "demo": "dm",
        "dev": "dv",
        "ml": "ml",
        "pre_prod": "pp",
        "prod": "pd",
        "quality_assurance": "qa",
        "sandbox": "sb",
        "security": "sc",
    }

    contexts = {"global": "gb", "shared": "sh"} | spokes | environments

    locations = AzureLocations.locations
    resources = ResourcesList.resources

    index_min_value = 0
    index_max_value = 99
    suffix_length = 2

    def __init__(self, workload: str, context: str, location: str):
        """
        Parameters
        ----------
        workload : str
            Name of the workload where the resource is created
        context : str
            Context where we want to create the resource. Can be global, a known spoke (hub, build, etc) or a known environment (dev, sandbox, prod, etc)
        location : str
            Location where we want to create the resource (eastus,westus2,...)
        """
        self.workload = workload
        self.context = context

        try:
            self.env = self.contexts[self.context]
        except KeyError:
            if self.context.endswith("-sandbox"):
                self.env = f"{self.context[:2]}-sb"
            else:
                raise KeyError(
                    f"Invalid context {self.context}. Valid contexts: {', '.join(self.contexts)}"
                )
        try:
            self.location = self.locations[location]
        except KeyError:
            raise KeyError(
                f"Unknown location {location}. Valid locations: {', '.join(self.locations)}"
            )

    def get(
        self,
        resource_name: str,
        suffix: int | str = 1,
        arbitrary: bool = False,
        dash_allowed: bool = True,
    ):
        """
        This class method returns the resource name abbreviation based on the format [resource-type]-[workload]-[env]-[location]-[suffix]

        If the argument `suffix` isn't passed in, the default value is 1
        If the resource does support dashes the name will be created with it, otherwise it will not use separators [resource-type]-[workload]-[env]-[location]-[suffix] or [resource-type][workload][env][location][suffix]

        Parameters
        ----------
        resource_name : str
            The name of the resource group in Azure
        suffix : int | str, optional
            The suffix of the resource, this is useful to create more than one resource of the same kind.
            Can be an integer index from 0-99 or 2 char long literal to name the resource
        arbitrary : bool, optional
            Overrides looking up the resource. Used for things that really aren't part of Azure
        dash_allowed: bool, optional
            Overrides the 'dash_allowed' property when the 'arbitrary' flag is set to True; otherwise, its value is ignored.
        """
        try:
            resource = self.resources[resource_name]
        except KeyError:
            if arbitrary:
                resource = {"abbr": resource_name, "dash_allowed": dash_allowed}
            else:
                raise KeyError(
                    f"unable to find resource {resource_name} in util.ResourceList"
                )

        max_length = cast(Optional[int], resource.get("max_length", None))

        if isinstance(suffix, int):
            if suffix < self.index_min_value or suffix > self.index_max_value:
                raise Exception(
                    f"Index '{suffix}' for resource '{resource_name}' is invalid. Should be in range {self.index_min_value}-{self.index_max_value}"
                )
            sequence = str(suffix).zfill(self.suffix_length)
        else:
            if not max_length and len(suffix) != self.suffix_length:
                raise Exception(
                    f"Suffix '{suffix}' for resource '{resource_name}' is not {self.suffix_length} characters long. To enable longer suffix, 'max_length' should be provided on resource definition"
                )
            sequence = suffix

        resource_abbr: str = resource["abbr"]
        separator = "-" if resource.get("dash_allowed") else ""
        resource_workload = (
            self.workload
            if resource.get("dash_allowed")
            else self.workload.replace("-", "")
        )

        name = f"{separator.join(filter(None, [self.prefix, resource_abbr, resource_workload, self.env, self.location, sequence]))}"

        if max_length and len(name) > max_length:
            raise Exception(
                f"Resource name: '{name}' is longer than defined max length ({max_length}). Try using a shorter suffix"
            )

        return name
