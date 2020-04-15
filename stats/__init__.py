from roll import Roll
from roll.extensions import simple_server

app = Roll()


@app.route('/stats/{parameter}', methods=["POST"])
async def stats(request, response, parameter):
    response.body = f'Hello {parameter}'


if __name__ == '__main__':
    simple_server(app)
