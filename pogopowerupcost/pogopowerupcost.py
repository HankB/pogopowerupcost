#!/usr/bin/env python3
# coding=utf-8

"""
Strategy to eliminate redundant lines.
- remove redundant lines
- calculate the correct key for a given level
"""

NORMAL_COST_PER_POWERUP = {
	# level: [stardust, candy]
	2.5:  [  200,  1],
	4.5:  [  400,  1],
	6.5:  [  600,  1],
	8.5:  [  800,  1],
	10.5: [ 1000,  1],
	12.5: [ 1300,  2],
	14.5: [ 1600,  2],
	16.5: [ 1900,  2],
	18.5: [ 2200,  2],
	20.5: [ 2500,  2],
	22.5: [ 3000,  3],
	24.5: [ 3500,  3],
	26.5: [ 4000,  3],
	28.5: [ 4500,  3],
	30.5: [ 5000,  4],
	32.5: [ 6000,  6],
	34.5: [ 7000,  8],
	36.5: [ 8000, 10],
	38.5: [ 9000, 12],
	40.5: [10000, 15], # Unconfirmed
}

SHADOW_COST_PER_POWERUP = {
	# level: [stardust, candy]
	2.5:  [  240,   2],
	4.5:  [  480,   2],
	6.5:  [  720,   2],
	8.5:  [  960,   2],
	10.5: [ 1200,   2],
	12.5: [ 1560,   3],
	14.5: [ 1920,   3],
	16.5: [ 2280,   3],
	18.5: [ 2640,   3],
	20.5: [ 3000,   3],
	22.5: [ 3600,   4],
	24.5: [ 4200,   4],
	26.5: [ 4800,   5],
	28.5: [ 5400,   5],
	30.5: [ 6000,   8],
	32.5: [ 7200,  10],
	34.5: [ 8400,  10],
	36.5: [ 9600,  12],
	38.5: [ 10800, 15],
	40.5: [ 12000, 18], # Unconfirmed
}

def calculate_powerup_cost(from_level, to_level, cost_table=NORMAL_COST_PER_POWERUP):
	total_stardust = 0
	total_candy = 0
	while from_level < to_level:
		table_key = from_level-((from_level+1) % 2)+1.5
		stardust, candy = cost_table[table_key]
		total_stardust += stardust
		total_candy += candy
		from_level += 0.5
	return {
		'stardust': total_stardust,
		'candy': total_candy,
	}
