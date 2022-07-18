import re
import pdb

def normalize_mac(mac_addr):

    normalized_addr = ""

    place_holder = 1
    for character in mac_addr.upper():
        if character == "." or character == "-":
            continue
        if place_holder in [3, 5, 7, 9, 11]:
            normalized_addr = normalized_addr + ":"
        normalized_addr = normalized_addr + character
        place_holder += 1

    return normalized_addr


def normalize2(mac_addr):
    good_mac = False
    match_patterns = [
        '\w{4}\.\w{4}\.\w{4}',
        '\w{2}-\w{2}-\w{2}-\w{2}-\w{2}-\w{2}'
    ]
    for pattern in match_patterns:
        search_result = re.search(pattern, mac_addr)
        if search_result:
            good_mac = True
            break

    if good_mac:
        working_addr = ""
        for character in mac_addr:
            if character in ['-', '.']:
                continue
            working_addr += character.upper()
        return(working_addr[:2] + ":" + working_addr[2:4] + ":" + working_addr[4:6] + ":" + working_addr[6:8] + ":" + working_addr[8:10] + ":" + working_addr[10:12])
    else:
        return None


def main():
    # print(normalize_mac('0000.aaaa.bbbb'))
    # print(normalize_mac('00-11-33-44-33-22'))
    # print(normalize_mac('00-11-bB-44-De-22'))
    pdb.set_trace()
    assert "33:CC:DD:88:77:33" == normalize2('33cc.dd88.7733'), f'Did not match'
    assert "33:CC:DD:88:77:32" == normalize2('33cc.dd88.7732'), f'Did not match'
    assert "33:CC:DD:88:77:31" == normalize2('33cc.dd88.7731'), f'Did not match'

if __name__ == "__main__":
    main()