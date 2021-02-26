#!/usr/bin/env python3
# coding=utf-8

from unittest import TestCase

from pogopowerupcost import calculate_powerup_cost

class TestHelper(TestCase):
	def test_1(self):
		for level in (1, 1.5, 2, 2.5):
			key = get_table_key(level)
			self.assertEqual(key, 2.5)

	def test_2(self):
		for level in (3, 3.5, 4, 4.5):
			key = get_table_key(level)
			self.assertEqual(key, 4.5)

	def test_3(self):
		for level in (5, 5.5, 6, 6.5):
			key = get_table_key(level)
			self.assertEqual(key, 6.5)

class TestCalculation(TestCase):

	def test_scenario_1(self):
		cost = calculate_powerup_cost(1, 20)
		self.assertEqual(cost['stardust'], 45000)
		self.assertEqual(cost['candy'], 56)

	def test_scenario_2(self):
		cost = calculate_powerup_cost(4.5, 20)
		self.assertEqual(cost['stardust'], 43000)
		self.assertEqual(cost['candy'], 49)

	def test_scenario_3(self):
		cost = calculate_powerup_cost(36.5, 39)
		self.assertEqual(cost['stardust'], 44000)
		self.assertEqual(cost['candy'], 58)

	def test_scenario_4(self):
		cost = calculate_powerup_cost(30.0, 38.5)
		self.assertEqual(cost['stardust'], 121000)
		self.assertEqual(cost['candy'], 140)

	def test_scenario_5(self):
		cost = calculate_powerup_cost(1, 1.5)
		self.assertEqual(cost['stardust'], 200)
		self.assertEqual(cost['candy'], 1)

	def test_scenario_6(self):
		cost = calculate_powerup_cost(1, 2)
		self.assertEqual(cost['stardust'], 400)
		self.assertEqual(cost['candy'], 2)

	def test_scenario_7(self):
		cost = calculate_powerup_cost(1, 2.5)
		self.assertEqual(cost['stardust'], 600)
		self.assertEqual(cost['candy'], 3)

	def test_scenario_8(self):
		cost = calculate_powerup_cost(1, 3)
		self.assertEqual(cost['stardust'], 800)
		self.assertEqual(cost['candy'], 4)

	def test_scenario_9(self):
		cost = calculate_powerup_cost(1, 3.5)
		self.assertEqual(cost['stardust'], 1200)
		self.assertEqual(cost['candy'], 5)
