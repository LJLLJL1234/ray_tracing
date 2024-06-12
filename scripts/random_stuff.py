import sys
sys.path.append('/Users/Lauri.Lehtola/private_projects/ray_tracing')
from src.utils import create_point

a = (1,2,3)
a_point = create_point(a)

print(a_point)