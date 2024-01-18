def serialize_dict(entity) -> dict:
    if entity != None:
        return {
            **{i: str(entity[i]) for i in entity if i in ['_id', 'image']},
            **{i: entity[i] for i in entity if not (i in ['_id', 'image'])},
        }
    return None


def serialize_list(entities) -> list:
    return [serialize_dict(entity) for entity in entities]
