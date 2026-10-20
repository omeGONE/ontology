from Instances import *

if __name__ == "__main__":
    objects = [obj for obj in globals().values() if isinstance(obj, Root)]

    def query_1_1(discipline):
        return [obj for obj in objects if isinstance(obj, Bike) and obj.createdFor is discipline]

    def query_1_n(cassette):
        return [obj for obj in objects if isinstance(obj, Sprocket) and obj.isPart is cassette]

    def query_transitive(bike):
        result = []
        for obj in objects:
            if obj is bike:
                continue
            node = obj
            while node is not None:
                if node is bike:
                    result.append(obj)
                    break
                node = getattr(node, "isPart", None)
        return result

    print("1:1:", [obj.name for obj in query_1_1(city)])
    print("1:N:", [obj.name for obj in query_1_n(shimano_hg200_marlin)])
    print("Транзитивный:", [obj.name for obj in query_transitive(trek_marlin)])