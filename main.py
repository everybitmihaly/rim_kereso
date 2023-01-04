from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()

templates = Jinja2Templates(directory=BASE_DIR / 'templates')


@app.get('/', response_class=HTMLResponse)
async def main_api(request: Request, first: str | None = None, second: str | None = None, third: str | None = None):

    # Querying comes here!

    return templates.TemplateResponse('main_template.html', {'request': request, 'data': {'first': first,
                                                                                          'second': second,
                                                                                          'third': third}
                                                             })
