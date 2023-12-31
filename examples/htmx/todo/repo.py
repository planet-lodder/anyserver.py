

class MockedRepository():
    FILTER = 'active'

    def all(self):
        return self.search('')

    def search(self, terms: str):
        found = MOCKED_DATA
        type = self.FILTER

        # Filter by search terms
        if len(terms):
            found = list(filter(lambda todo: terms in todo["title"], found))

        # Filter by todo status
        match type:
            case "active":
                found = list(filter(lambda todo: not todo["completed"], found))
            case "completed":
                found = list(filter(lambda todo: todo["completed"], found))

        return found

    def find(self, task_id: int):
        search = list(filter(lambda todo: int(
            task_id) == todo["id"], MOCKED_DATA))
        found = search[0] if len(search) else None
        return found

    def remove(self, task_id: int):
        found = self.find(task_id)
        if found:
            MOCKED_DATA.remove(found)
        return found

    def clear(self):
        found = []
        match self.FILTER:
            case "active":
                # Clear all active items
                found = list(
                    filter(lambda todo: not todo["completed"], MOCKED_DATA))
            case "completed":
                # Clear completed items
                found = list(
                    filter(lambda todo: todo["completed"], MOCKED_DATA))
            case "all":
                found = list(filter(lambda todo: todo, MOCKED_DATA))
        for todo in found:
            MOCKED_DATA.remove(todo)
        return MOCKED_DATA


MOCKED_DATA = [
    {"userId": 1, "id": 1, "title": "delectus aut autem", "completed": False},
    {
        "userId": 1,
        "id": 2,
        "title": "quis ut nam facilis et officia qui",
        "completed": False,
    },
    {"userId": 1, "id": 3, "title": "fugiat veniam minus", "completed": False},
    {"userId": 1, "id": 4, "title": "et porro tempora", "completed": True},
    {
        "userId": 1,
        "id": 5,
        "title": "laboriosam mollitia et enim quasi adipisci quia provident illum",
        "completed": False,
    },
    {
        "userId": 1,
        "id": 6,
        "title": "qui ullam ratione quibusdam voluptatem quia omnis",
        "completed": False,
    },
    {
        "userId": 1,
        "id": 7,
        "title": "illo expedita consequatur quia in",
        "completed": False,
    },
    {"userId": 1, "id": 8, "title": "quo adipisci enim quam ut ab", "completed": True},
    {"userId": 1, "id": 9, "title": "molestiae perspiciatis ipsa", "completed": False},
    {
        "userId": 1,
        "id": 10,
        "title": "illo est ratione doloremque quia maiores aut",
        "completed": True,
    },
    {"userId": 1, "id": 11, "title": "vero rerum temporibus dolor", "completed": True},
    {"userId": 1, "id": 12, "title": "ipsa repellendus fugit nisi", "completed": True},
    {"userId": 1, "id": 13, "title": "et doloremque nulla", "completed": False},
    {
        "userId": 1,
        "id": 14,
        "title": "repellendus sunt dolores architecto voluptatum",
        "completed": True,
    },
    {"userId": 1, "id": 15, "title": "ab voluptatum amet voluptas", "completed": True},
    {
        "userId": 1,
        "id": 16,
        "title": "accusamus eos facilis sint et aut voluptatem",
        "completed": True,
    },
    {
        "userId": 1,
        "id": 17,
        "title": "quo laboriosam deleniti aut qui",
        "completed": True,
    },
    {
        "userId": 1,
        "id": 18,
        "title": "dolorum est consequatur ea mollitia in culpa",
        "completed": False,
    },
    {
        "userId": 1,
        "id": 19,
        "title": "molestiae ipsa aut voluptatibus pariatur dolor nihil",
        "completed": True,
    },
    {
        "userId": 1,
        "id": 20,
        "title": "ullam nobis libero sapiente ad optio sint",
        "completed": True,
    },
    {
        "userId": 2,
        "id": 21,
        "title": "suscipit repellat esse quibusdam voluptatem incidunt",
        "completed": False,
    },
    {
        "userId": 2,
        "id": 22,
        "title": "distinctio vitae autem nihil ut molestias quo",
        "completed": True,
    },
    {
        "userId": 2,
        "id": 23,
        "title": "et itaque necessitatibus maxime molestiae qui quas velit",
        "completed": False,
    },
    {
        "userId": 2,
        "id": 24,
        "title": "adipisci non ad dicta qui amet quaerat doloribus ea",
        "completed": False,
    },
    {
        "userId": 2,
        "id": 25,
        "title": "voluptas quo tenetur perspiciatis explicabo natus",
        "completed": True,
    },
    {"userId": 2, "id": 26, "title": "aliquam aut quasi", "completed": True},
    {"userId": 2, "id": 27, "title": "veritatis pariatur delectus", "completed": True},
    {
        "userId": 2,
        "id": 28,
        "title": "nesciunt totam sit blanditiis sit",
        "completed": False,
    },
    {"userId": 2, "id": 29, "title": "laborum aut in quam", "completed": False},
    {
        "userId": 2,
        "id": 30,
        "title": "nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis",
        "completed": True,
    },
    {
        "userId": 2,
        "id": 31,
        "title": "repudiandae totam in est sint facere fuga",
        "completed": False,
    },
    {
        "userId": 2,
        "id": 32,
        "title": "earum doloribus ea doloremque quis",
        "completed": False,
    },
    {"userId": 2, "id": 33, "title": "sint sit aut vero", "completed": False},
    {
        "userId": 2,
        "id": 34,
        "title": "porro aut necessitatibus eaque distinctio",
        "completed": False,
    },
    {
        "userId": 2,
        "id": 35,
        "title": "repellendus veritatis molestias dicta incidunt",
        "completed": True,
    },
    {
        "userId": 2,
        "id": 36,
        "title": "excepturi deleniti adipisci voluptatem et neque optio illum ad",
        "completed": True,
    },
    {"userId": 2, "id": 37, "title": "sunt cum tempora", "completed": False},
    {"userId": 2, "id": 38, "title": "totam quia non", "completed": False},
    {
        "userId": 2,
        "id": 39,
        "title": "doloremque quibusdam asperiores libero corrupti illum qui omnis",
        "completed": False,
    },
    {"userId": 2, "id": 40, "title": "totam atque quo nesciunt", "completed": True},
    {
        "userId": 3,
        "id": 41,
        "title": "aliquid amet impedit consequatur aspernatur placeat eaque fugiat suscipit",
        "completed": False,
    },
    {
        "userId": 3,
        "id": 42,
        "title": "rerum perferendis error quia ut eveniet",
        "completed": False,
    },
    {
        "userId": 3,
        "id": 43,
        "title": "tempore ut sint quis recusandae",
        "completed": True,
    },
    {
        "userId": 3,
        "id": 44,
        "title": "cum debitis quis accusamus doloremque ipsa natus sapiente omnis",
        "completed": True,
    },
    {
        "userId": 3,
        "id": 45,
        "title": "velit soluta adipisci molestias reiciendis harum",
        "completed": False,
    },
    {
        "userId": 3,
        "id": 46,
        "title": "vel voluptatem repellat nihil placeat corporis",
        "completed": False,
    },
    {
        "userId": 3,
        "id": 47,
        "title": "nam qui rerum fugiat accusamus",
        "completed": False,
    },
    {
        "userId": 3,
        "id": 48,
        "title": "sit reprehenderit omnis quia",
        "completed": False,
    },
    {
        "userId": 3,
        "id": 49,
        "title": "ut necessitatibus aut maiores debitis officia blanditiis velit et",
        "completed": False,
    },
    {
        "userId": 3,
        "id": 50,
        "title": "cupiditate necessitatibus ullam aut quis dolor voluptate",
        "completed": True,
    },
    {
        "userId": 3,
        "id": 51,
        "title": "distinctio exercitationem ab doloribus",
        "completed": False,
    },
    {
        "userId": 3,
        "id": 52,
        "title": "nesciunt dolorum quis recusandae ad pariatur ratione",
        "completed": False,
    },
    {
        "userId": 3,
        "id": 53,
        "title": "qui labore est occaecati recusandae aliquid quam",
        "completed": False,
    },
    {
        "userId": 3,
        "id": 54,
        "title": "quis et est ut voluptate quam dolor",
        "completed": True,
    },
    {
        "userId": 3,
        "id": 55,
        "title": "voluptatum omnis minima qui occaecati provident nulla voluptatem ratione",
        "completed": True,
    },
    {"userId": 3, "id": 56, "title": "deleniti ea temporibus enim", "completed": True},
    {
        "userId": 3,
        "id": 57,
        "title": "pariatur et magnam ea doloribus similique voluptatem rerum quia",
        "completed": False,
    },
    {
        "userId": 3,
        "id": 58,
        "title": "est dicta totam qui explicabo doloribus qui dignissimos",
        "completed": False,
    },
    {
        "userId": 3,
        "id": 59,
        "title": "perspiciatis velit id laborum placeat iusto et aliquam odio",
        "completed": False,
    },
    {
        "userId": 3,
        "id": 60,
        "title": "et sequi qui architecto ut adipisci",
        "completed": True,
    },
    {"userId": 4, "id": 61, "title": "odit optio omnis qui sunt", "completed": True},
    {
        "userId": 4,
        "id": 62,
        "title": "et placeat et tempore aspernatur sint numquam",
        "completed": False,
    },
    {
        "userId": 4,
        "id": 63,
        "title": "doloremque aut dolores quidem fuga qui nulla",
        "completed": True,
    },
    {
        "userId": 4,
        "id": 64,
        "title": "voluptas consequatur qui ut quia magnam nemo esse",
        "completed": False,
    },
    {
        "userId": 4,
        "id": 65,
        "title": "fugiat pariatur ratione ut asperiores necessitatibus magni",
        "completed": False,
    },
    {
        "userId": 4,
        "id": 66,
        "title": "rerum eum molestias autem voluptatum sit optio",
        "completed": False,
    },
    {
        "userId": 4,
        "id": 67,
        "title": "quia voluptatibus voluptatem quos similique maiores repellat",
        "completed": False,
    },
    {
        "userId": 4,
        "id": 68,
        "title": "aut id perspiciatis voluptatem iusto",
        "completed": False,
    },
    {
        "userId": 4,
        "id": 69,
        "title": "doloribus sint dolorum ab adipisci itaque dignissimos aliquam suscipit",
        "completed": False,
    },
    {
        "userId": 4,
        "id": 70,
        "title": "ut sequi accusantium et mollitia delectus sunt",
        "completed": False,
    },
    {"userId": 4, "id": 71, "title": "aut velit saepe ullam", "completed": False},
    {
        "userId": 4,
        "id": 72,
        "title": "praesentium facilis facere quis harum voluptatibus voluptatem eum",
        "completed": False,
    },
    {
        "userId": 4,
        "id": 73,
        "title": "sint amet quia totam corporis qui exercitationem commodi",
        "completed": True,
    },
    {
        "userId": 4,
        "id": 74,
        "title": "expedita tempore nobis eveniet laborum maiores",
        "completed": False,
    },
    {
        "userId": 4,
        "id": 75,
        "title": "occaecati adipisci est possimus totam",
        "completed": False,
    },
    {"userId": 4, "id": 76, "title": "sequi dolorem sed", "completed": True},
    {
        "userId": 4,
        "id": 77,
        "title": "maiores aut nesciunt delectus exercitationem vel assumenda eligendi at",
        "completed": False,
    },
    {
        "userId": 4,
        "id": 78,
        "title": "reiciendis est magnam amet nemo iste recusandae impedit quaerat",
        "completed": False,
    },
    {"userId": 4, "id": 79, "title": "eum ipsa maxime ut", "completed": True},
    {
        "userId": 4,
        "id": 80,
        "title": "tempore molestias dolores rerum sequi voluptates ipsum consequatur",
        "completed": True,
    },
    {"userId": 5, "id": 81, "title": "suscipit qui totam", "completed": True},
    {
        "userId": 5,
        "id": 82,
        "title": "voluptates eum voluptas et dicta",
        "completed": False,
    },
    {
        "userId": 5,
        "id": 83,
        "title": "quidem at rerum quis ex aut sit quam",
        "completed": True,
    },
    {"userId": 5, "id": 84, "title": "sunt veritatis ut voluptate", "completed": False},
    {"userId": 5, "id": 85, "title": "et quia ad iste a", "completed": True},
    {"userId": 5, "id": 86, "title": "incidunt ut saepe autem", "completed": True},
    {
        "userId": 5,
        "id": 87,
        "title": "laudantium quae eligendi consequatur quia et vero autem",
        "completed": True,
    },
    {
        "userId": 5,
        "id": 88,
        "title": "vitae aut excepturi laboriosam sint aliquam et et accusantium",
        "completed": False,
    },
    {"userId": 5, "id": 89, "title": "sequi ut omnis et", "completed": True},
    {
        "userId": 5,
        "id": 90,
        "title": "molestiae nisi accusantium tenetur dolorem et",
        "completed": True,
    },
    {
        "userId": 5,
        "id": 91,
        "title": "nulla quis consequatur saepe qui id expedita",
        "completed": True,
    },
    {"userId": 5, "id": 92, "title": "in omnis laboriosam", "completed": True},
    {
        "userId": 5,
        "id": 93,
        "title": "odio iure consequatur molestiae quibusdam necessitatibus quia sint",
        "completed": True,
    },
    {"userId": 5, "id": 94, "title": "facilis modi saepe mollitia", "completed": False},
    {
        "userId": 5,
        "id": 95,
        "title": "vel nihil et molestiae iusto assumenda nemo quo ut",
        "completed": True,
    },
    {
        "userId": 5,
        "id": 96,
        "title": "nobis suscipit ducimus enim asperiores voluptas",
        "completed": False,
    },
    {
        "userId": 5,
        "id": 97,
        "title": "dolorum laboriosam eos qui iure aliquam",
        "completed": False,
    },
    {
        "userId": 5,
        "id": 98,
        "title": "debitis accusantium ut quo facilis nihil quis sapiente necessitatibus",
        "completed": True,
    },
    {"userId": 5, "id": 99, "title": "neque voluptates ratione", "completed": False},
    {
        "userId": 5,
        "id": 100,
        "title": "excepturi a et neque qui expedita vel voluptate",
        "completed": False,
    },
]
