'''OpenGL extension NV.fragment_program

This module customises the behaviour of the 
OpenGL.raw.GL.NV.fragment_program to provide a more 
Python-friendly API

Overview (from the spec)
	
	OpenGL mandates a certain set of configurable per-fragment computations
	defining texture lookup, texture environment, color sum, and fog
	operations.  Each of these areas provide a useful but limited set of fixed
	operations.  For example, unextended OpenGL 1.2.1 provides only four
	texture environment modes, color sum, and three fog modes.  Many OpenGL
	extensions have either improved existing functionality or introduced new
	configurable fragment operations.  While these extensions have enabled new
	and interesting rendering effects, the set of effects is limited by the
	set of special modes introduced by the extension.  This lack of
	flexibility is in contrast to the high-level of programmability of
	general-purpose CPUs and other (frequently software-based) shading
	languages.  The purpose of this extension is to expose to the OpenGL
	application writer an unprecedented degree of programmability in the
	computation of final fragment colors and depth values.
	
	This extension provides a mechanism for defining fragment program
	instruction sequences for application-defined fragment programs.  When in
	fragment program mode, a program is executed each time a fragment is
	produced by rasterization.  The inputs for the program are the attributes
	(position, colors, texture coordinates) associated with the fragment and a
	set of constant registers.  A fragment program can perform mathematical
	computations and texture lookups using arbitrary texture coordinates.  The
	results of a fragment program are new color and depth values for the
	fragment.
	
	This extension defines a programming model including a 4-component vector
	instruction set, 16- and 32-bit floating-point data types, and a
	relatively large set of temporary registers.  The programming model also
	includes a condition code vector which can be used to mask register writes
	at run-time or kill fragments altogether.  The syntax, program
	instructions, and general semantics are similar to those in the
	NV_vertex_program and NV_vertex_program2 extensions, which provide for the
	execution of an arbitrary program each time the GL receives a vertex.
	
	The fragment program execution environment is designed for efficient
	hardware implementation and to support a wide variety of programs.  By
	design, the entire set of existing fragment programs defined by existing
	OpenGL per-fragment computation extensions can be implemented using the
	extension's programming model.
	
	The fragment program execution environment accesses textures via
	arbitrarily computed texture coordinates.  As such, there is no necessary
	correspondence between the texture coordinates and texture maps previously
	lumped into a single "texture unit".  This extension separates the notion
	of "texture coordinate sets" and "texture image units" (texture maps and
	associated parameters), allowing implementations with a different number
	of each.  The initial implementation of this extension will support 8
	texture coordinate sets and 16 texture image units.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/NV/fragment_program.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.NV.fragment_program import *
from OpenGL.raw.GL.NV.fragment_program import _EXTENSION_NAME

def glInitFragmentProgramNV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

glProgramNamedParameter4fNV=wrapper.wrapper(glProgramNamedParameter4fNV).setInputArraySize(
    'name', 1
)
glProgramNamedParameter4fvNV=wrapper.wrapper(glProgramNamedParameter4fvNV).setInputArraySize(
    'name', 1
).setInputArraySize(
    'v', 4
)
glProgramNamedParameter4dNV=wrapper.wrapper(glProgramNamedParameter4dNV).setInputArraySize(
    'name', 1
)
glProgramNamedParameter4dvNV=wrapper.wrapper(glProgramNamedParameter4dvNV).setInputArraySize(
    'name', 1
).setInputArraySize(
    'v', 4
)
glGetProgramNamedParameterfvNV=wrapper.wrapper(glGetProgramNamedParameterfvNV).setInputArraySize(
    'name', 1
).setOutput(
    'params',size=(4,),orPassIn=True
)
glGetProgramNamedParameterdvNV=wrapper.wrapper(glGetProgramNamedParameterdvNV).setInputArraySize(
    'name', 1
).setOutput(
    'params',size=(4,),orPassIn=True
)
### END AUTOGENERATED SECTION