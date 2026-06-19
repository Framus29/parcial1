from pydantic import BaseModel, Field
from typing import Annotated

# 1. Vista de edición/creación (NO incluye id)
class ArticuloBase(BaseModel):
    titulo: Annotated[str, Field(min_length=3, description="Título del artículo")]
    descripcion: Annotated[str, Field(min_length=3, description="Descripción del artículo")]
    precio: Annotated[float, Field(ge=0, description="Precio del artículo")]

# 2. Vista de respuesta general (SÍ incluye id)
class ArticuloRespuesta(ArticuloBase):
    id: Annotated[int, Field(ge=1, description="ID único del artículo")]