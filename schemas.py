from pydantic import BaseModel, Field, EmailStr

class RegisterRequest(BaseModel):
    name: str = Field(min_length=2, max_length=80)
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class TextRequest(BaseModel):
    text: str = Field(min_length=1, max_length=10000)

class URLRequest(BaseModel):
    url: str = Field(min_length=3, max_length=5000)

class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=4000)

class LessonRequest(BaseModel):
    lesson_id: int

class QuizRequest(BaseModel):
    answer: str
