from typing import List

from models.roomManager import RoomManager

coords = {
    1: [(195, 40), (240, 40), (195, 85), (240, 85)],
    2: [(330, 40), (375, 40), (330, 85), (375, 85)],
    3: [(465, 40), (510, 40), (465, 85), (510, 85)],
    4: [(595, 40), (640, 40), (595, 85), (640, 85)],
    5: [(195, 320), (240, 320), (195, 365), (240, 365)],
    6: [(330, 320), (375, 320), (330, 365), (375, 365)],
    7: [(465, 320), (510, 320), (465, 365), (510, 365)],
    8: [(595, 320), (640, 320), (595, 365), (640, 365)],
}


def get_indicators(section_number: int) -> List[tuple]:
    result = list()

    for room in RoomManager.all_rooms(section_number):
        coords_arr = coords[room.room_number]
        counter = 4 - room.free_of_beds

        for x_axis, y_axis in coords_arr:
            if counter != 4:
                if counter:
                    result.append((x_axis, y_axis, 'red'))
                    counter -= 1
                else:
                    result.append((x_axis, y_axis, '#00FF00'))
            else:
                result.append((x_axis, y_axis, '#00FF00'))

    return result
