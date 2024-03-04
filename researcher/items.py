from typing import Union

from pydantic import BaseModel, Field, HttpUrl, model_serializer, model_validator
from pydantic.networks import EmailStr, validate_email
from pydantic_core._pydantic_core import PydanticCustomError


class USTBResearcherItem(BaseModel):
    name: str
    title: str
    departments: list[str] = Field(default_factory=list)
    mail: Union[EmailStr, None] = Field(default=None)
    research_interests: list[str] = Field(default_factory=list)
    link: HttpUrl

    @model_validator(mode="before")
    @classmethod
    def validate_item(self, data) -> str:
        data["name"] = data["name"].strip()
        data["title"] = data["title"].strip()

        if data["mail"]:
            try:
                _, data["mail"] = validate_email(data["mail"].strip())
            except PydanticCustomError:
                data["mail"] = None

        data["departments"] = list(filter(lambda x: x != "", data["departments"].split("|")))
        data["research_interests"] = data["research_interests"].split(";") if data["research_interests"] else []
        return data

    @model_serializer()
    def serialize_model(self) -> dict:
        return {
            "name": self.name,
            "title": self.title,
            "departments": ",".join(self.departments),
            "mail": self.mail,
            "research_interests": "; ".join(self.research_interests),
            "link": str(self.link),
        }
