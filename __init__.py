from get_rectangle_infos import get_rectangle_information


def intersects(box1, box2):
    box1 = get_rectangle_information(box1).format_1x4
    box2 = get_rectangle_information(box2).format_1x4
    return not (
        box1[2] < box2[0] or box1[0] > box2[2] or box1[1] > box2[3] or box1[3] < box2[1]
    )

