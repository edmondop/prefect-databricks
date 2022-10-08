"""This is an example blocks module"""

from prefect.blocks.core import Block
from pydantic import Field


class DatabricksBlock(Block):
    """
    A sample block that holds a value.

    Attributes:
        value (str): The value to store.

    Example:
        Load a stored value:
        ```python
        from prefect_databricks import DatabricksBlock
        block = DatabricksBlock.load("BLOCK_NAME")
        ```
    """

    _block_type_name = "databricks"
    # _logo_url = "https://path/to/logo.png"

    value: str = Field("The default value", description="The value to store")

    @classmethod
    def seed_value_for_example(cls):
        """
        Seeds the field, value, so the block can be loaded.
        """
        block = cls(value="A sample value")
        block.save("sample-block", overwrite=True)
