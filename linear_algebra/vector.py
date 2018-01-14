from math import sqrt,acos,pi
from decimal import Decimal,getcontext

getcontext().prec = 30

class Vector(object):

	CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector'

	def __getitem__(self,index):
		return self.coordinates[index]

	def __init__(self, coordinates):
		try:
			if not coordinates:
				raise ValueError
			self.coordinates = tuple([Decimal(x) for x in coordinates])
			self.dimention = len(self.coordinates)

		except ValueError:
			raise ValueError('The coordinates must be nonempty')

		except TypeError:
			raise TypeError('The coordinates must be an iterable number')

	def __str__(self):
		return 'Vector: {}'.format(self.coordinates)

	def __eq__(self, v):
		return self.coordinates == v.coordinates

	def plus(self, v):
		new_coordinates = [x+y for x,y in zip(self.coordinates,v.coordinates)]
		return Vector(new_coordinates)

	def minus(self, v):
		new_coordinates = [x-y for x,y in zip(self.coordinates,v.coordinates)]
		return Vector(new_coordinates)

	def times_scalar(self,c):
		new_coordinates = [Decimal(c)*x for x in self.coordinates]
		return Vector(new_coordinates)

	def magnitude(self):
		coordinates_squared = [x**2 for x in self.coordinates]
		#return sqrt(sum(coordinates_squared))
		return sum(coordinates_squared).sqrt()

	def normalized(self):
		try:
			magnitude = self.magnitude()
			return self.times_scalar(Decimal(1.0)/Decimal(magnitude))

		except ZeroDivisionError:
			raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)

	def is_orthogonal_to(self,v,tolerance=1e-10):
		return abs(self.dot(v)) < tolerance

	def is_parallel_to(self,v):
		return ( self.is_zero() or
			v.is_zero() or
			self.angle_with(v) == 0 or
			self.angle_with(v) == pi)

	def is_zero(self,tolerance=1e-10):
		return self.magnitude() < tolerance

	def dot(self,v): 
		return sum([x*y for x,y in zip(self.coordinates,v.coordinates)])


	def angle_with(self,v,in_degrees=False):
		try:
			u1 = self.normalized()
			u2 = v.normalized()
			angle_in_radians = acos(u1.dot(u2))

			if in_degrees:
				degrees_per_radian = Decimal(180.0) / Decimal(pi)
				return Decimal(angle_in_radians) * degrees_per_radian
			else:
				return angle_in_radians
		
		except Exception as e:
			if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
				raise Exception('cannot compute an angle with zero vector~!')
			else:
				raise e
	
	def component_orthogonal_to(self, basis):
		try:
			projection = self.component_parallel_to(basis)
			return self.minus(projection)

		except Exception as e:
			raise e


	def component_parallel_to(self, basis):
		try:
			u =basis.normalized()
			weight = self.dot(u)
			return u.times_scalar(weight)

		except Exception as e:
			raise e

	def cross(self, v):
		try:
			x1,y1,z1 = self.coordinates
			x2,y2,z2 = v.coordinates
			new_coordinates = [ y1*z2 - y2*z1,
			-(x1*z2 - x2*z1),
			x1*y2 - x2*y1]
			return Vector(new_coordinates)
		except Exception as e:
			raise e
	def area_of_parallelogram_with(self,v):
		cross_product = self.cross(v)
		return cross_product.magnitude()

	def area_of_traiangle_with(self,v):
		return self.area_of_parallelogram_with(v) / Decimal('2.0')


'''
v = Vector(['-7.579','-7.88'])
w = Vector(['22.737','23.64'])

print "v vector is :" + str(v)

print v.is_parallel_to(w)
print v.is_orthogonal_to(w)

v = Vector([-5.955,-4.904,-1.874])
w = Vector([-4.496,-8.755,7.103])

print v.dot(w)

v = Vector(['3.183','-7.627'])
w = Vector(['-2.668','5.319'])

print v.angle_with(w)

v = Vector(['7.35','0.221','5.188'])
w = Vector(['2.751','8.259','3.985'])

print v.angle_with(w,True)

v = Vector([3.039,1.879])
w = Vector([0.825,2.036])
print v.component_parallel_to(w)
print v.component_orthogonal_to(w)

v = Vector([1,2,3])
w = Vector([4,2,1])
print v.cross(w)
print v.area_of_parallelogram_with(w)
'''