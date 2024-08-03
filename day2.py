import re

s = 'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'
print(s)


def parse_game(s):
    game, cubes = s.split(':')
    _, id = game.split()
    x = parse_sets(cubes)
    return {
        'id': int(id),
        'cubes': parse_sets(cubes)
    }


def parse_sets(s):
    cubes = re.findall(r'(\d+) ([a-z]+)', s)
    return [(int(x[0]), x[1]) for x in cubes]


bag = {
    'red': 12,
    'green': 13,
    'blue': 14
}

g = parse_game(s)


def possible_game(game, bag):
    return all(x[0] <= bag[x[1]] for x in game['cubes'])


assert possible_game(g, bag)

g = parse_game('Game 1: 13 red')
assert not possible_game(g, bag)

valid_games = filter(lambda x: possible_game(x, bag), map(parse_game, open('day2.txt').readlines()))
print(sum(x['id'] for x in valid_games))
