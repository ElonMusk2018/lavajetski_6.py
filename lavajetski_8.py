# Base project format.
# put this on the desktop : git clone https://github.com/tritechsc/mcpi
from mcpi.minecraft import Minecraft
from mcpi import block
from mcpi import event
from time import sleep
from random import randint
import math

def init():
    mc = Minecraft.create("127.0.0.1", 4711)
    x, y, z = mc.player.getPos()		
    return mc

def clear_with_air_up(mc, x, y, z,h,k,l):
	air = 0;
	mc.setBlocks(x-h,y,z-l,x+h,y+k,z+l,air)	

def ring(mc,xs,ys,zs,r):
	y = ys
	count = 0
	for t in range (0,360,15):
		radians = (t * (3.141592/180))
		rval=randint(1,20)
		x = math.cos(radians) * r
		z = math.sin(radians) * r
		# raval is random number  and wc will be wool color
		wc = count % 7
		count = count +1
		mc.setBlocks(x,y,z,x,y+rval,z,35,wc)	
		print(t,x,y)
		
def boat(mc,xs,ys,zs):
	m = 42
	o = 0
	l = 49
	t = 10
	f = 89
	g = 246
	r = 247
	mc.setBlocks(xs, ys, zs+2, xs,ys,zs+12,l)# 0
	mc.setBlocks(xs-1, ys+1, zs+2, xs+1,ys+1,zs+13,l) #1
	mc.setBlocks(xs, ys+1, zs+2, xs,ys+1,zs+14,l)# 1
	mc.setBlocks(xs-2, ys+2, zs+2, xs+2,ys+2,zs+14,l) #2
	#mc.setBlocks(xs, ys, zs+2, xs,ys+2,zs+15,m)# 2
	mc.setBlocks(xs-1, ys+3, zs+14, xs+1, ys+3, zs+2,l) #3
	mc.setBlocks(xs-1, ys+4, zs+8, xs+1, ys+4, zs+2,l) #3
	mc.setBlocks(xs-1, ys+4, zs+12, xs+1, ys+4, zs+8,l) #3(backside)
	mc.setBlocks(xs-0, ys+5, zs+12, xs-0, ys+5, zs+5,l) #3(backside)
	mc.setBlocks(xs-0, ys+4, zs+5, xs-0, ys+4, zs+2,l) #3(backside)WORK IN PROGRESS
	mc.setBlocks(xs-1, ys+5, zs+8, xs+1, ys+5, zs+5,l) #4
	mc.setBlocks(xs-0, ys+5, zs+7, xs-0, ys+5, zs+5,t) #4
	mc.setBlocks(xs-1, ys+5, zs+3, xs+1, ys+5, zs+2,l) #4
	mc.setBlocks(xs-1, ys+6, zs+3, xs+1, ys+6, zs+2,l) #5
	mc.setBlocks(xs-5, ys+6, zs+2, xs+5, ys+6, zs+2,l) #5
	mc.setBlocks(xs-1, ys+7, zs+3, xs+1, ys+7, zs+3,l) #6
	mc.setBlocks(xs-1, ys+7, zs+2, xs+1, ys+7, zs+2,l) #6
	mc.setBlocks(xs-0, ys+8, zs+2, xs+0, ys+8, zs+2,l) #7
	#(fins)
	mc.setBlocks(xs-3, ys+2, zs+12, xs-3, ys+2, zs+14,g) #(lefst fin connector)
	mc.setBlocks(xs-4, ys+3, zs+11, xs-4, ys+1, zs+15,g) #(left fin)
	mc.setBlocks(xs-5, ys+2, zs+11, xs-5, ys+2, zs+15,g) #(left fin 2)
	mc.setBlocks(xs+3, ys+2, zs+12, xs+3, ys+2, zs+14,g) #(right fin connector)
	mc.setBlocks(xs+4, ys+3, zs+11, xs+4, ys+1, zs+15,g) #(right fin)
	mc.setBlocks(xs+5, ys+2, zs+11, xs+5, ys+2, zs+15,g) #(right fin 2)
	#(front)
	mc.setBlocks(xs-1, ys+1, zs+1, xs+1, ys+6, zs+3,l) #(front)
	mc.setBlocks(xs-0, ys+0, zs+1, xs-0, ys+7, zs+3,l) #(front line)
	mc.setBlocks(xs-1, ys+2, zs-0, xs+1, ys+5, zs+3,l) #(front 2nd layer)
	mc.setBlocks(xs-0, ys+1, zs+0, xs-0, ys+6, zs+3,l) #(front 2nd line)
	mc.setBlocks(xs-0, ys+2, zs-1, xs-0, ys+5, zs+3,l) #(front 3rd line)
	#(front-decorations)
	mc.setBlocks(xs+1, ys+7, zs+1, xs+1, ys+7, zs+1,f)
	mc.setBlocks(xs-1, ys+7, zs+1, xs-1, ys+7, zs+1,f)
	#(extra)
	mc.setBlocks(xs-0, ys+4, zs+13, xs+0, ys+4, zs+14,l)
	mc.setBlocks(xs-1, ys+2, zs+15, xs+1, ys+2, zs+15,l)
	mc.setBlocks(xs-2, ys+3, zs+12, xs-2, ys+3, zs+5,l)
	mc.setBlocks(xs+2, ys+3, zs+12, xs+2, ys+3, zs+5,l)
	mc.setBlocks(xs+2, ys+4, zs+7, xs+2, ys+4, zs+6,l)
	mc.setBlocks(xs-2, ys+4, zs+7, xs-2, ys+4, zs+6,l)
	mc.setBlocks(xs-0, ys+6, zs+12, xs-0, ys+6, zs+9,l)
	mc.setBlocks(xs-0, ys+5, zs+14, xs-0, ys+5, zs+9,l)
	mc.setBlocks(xs-0, ys+4, zs+15, xs-0, ys+3, zs+15,l)
	mc.setBlocks(xs-0, ys+3, zs+16, xs-0, ys+2, zs+16,l)
	mc.setBlocks(xs-0, ys+2, zs+17, xs-0, ys+2, zs+18,l)
	mc.setBlocks(xs-0, ys+3, zs+18, xs-0, ys+3, zs+18,l)
	mc.setBlocks(xs-0, ys+4, zs+18, xs-0, ys+4, zs+18,g)
	mc.setBlocks(xs-0, ys+5, zs+18, xs-0, ys+5, zs+18,t)
	#(lava_holes)
	mc.setBlocks(xs-4, ys+2, zs+16, xs-4, ys+2, zs+16,t)
	mc.setBlocks(xs+4, ys+2, zs+16, xs+4, ys+2, zs+16,t)
		
def main():
	mc = init()
	x, y, z = mc.player.getPos()	
	ring(mc,x,y,z,5)
	ring(mc,x,y,z,10)
	ring(mc,x,y,z,15)	
main()

# multiple line comment
"""
AIR                   0
STONE                 1
GRASS                 2
DIRT                  3
COBBLESTONE           4
WOOD_PLANKS           5
SAPLING               6
BEDROCK               7
WATER_FLOWING         8
WATER                 8
WATER_STATIONARY      9
LAVA_FLOWING         10
LAVA                 10
LAVA_STATIONARY      11
SAND                 12
GRAVEL               13
GOLD_ORE             14
IRON_ORE             15
COAL_ORE             16
WOOD                 17
LEAVES               18
GLASS                20
LAPIS_LAZULI_ORE     21
LAPIS_LAZULI_BLOCK   22
SANDSTONE            24
BED                  26
COBWEB               30
GRASS_TALL           31
WOOL                 35
FLOWER_YELLOW        37
FLOWER_CYAN          38
MUSHROOM_BROWN       39
MUSHROOM_RED         40
GOLD_BLOCK           41
IRON_BLOCK           42
STONE_SLAB_DOUBLE    43
STONE_SLAB           44
BRICK_BLOCK          45
TNT                  46
BOOKSHELF            47
MOSS_STONE           48
OBSIDIAN             49
TORCH                50
FIRE                 51
STAIRS_WOOD          53
CHEST                54
DIAMOND_ORE          56
DIAMOND_BLOCK        57
CRAFTING_TABLE       58
FARMLAND             60
FURNACE_INACTIVE     61
FURNACE_ACTIVE       62
DOOR_WOOD            64
LADDER               65
STAIRS_COBBLESTONE   67
DOOR_IRON            71
REDSTONE_ORE         73
SNOW                 78
ICE                  79
SNOW_BLOCK           80
CACTUS               81
CLAY                 82
SUGAR_CANE           83
FENCE                85
GLOWSTONE_BLOCK      89
BEDROCK_INVISIBLE    95
STONE_BRICK          98
GLASS_PANE          102
MELON               103
FENCE_GATE          107
GLOWING_OBSIDIAN    246
NETHER_REACTOR_CORE 247
"""
