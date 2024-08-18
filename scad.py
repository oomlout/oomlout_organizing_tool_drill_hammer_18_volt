import copy
import opsc
import oobb
import oobb_base

def main(**kwargs):
    make_scad(**kwargs)

def make_scad(**kwargs):
    parts = []

    # save_type variables
    if True:
        filter = ""
        #filter = "test"

        #kwargs["save_type"] = "none"
        kwargs["save_type"] = "all"
        
        kwargs["overwrite"] = True
        
        #kwargs["modes"] = ["3dpr", "laser", "true"]
        kwargs["modes"] = ["3dpr"]
        #kwargs["modes"] = ["laser"]

    # default variables
    if True:
        kwargs["size"] = "oobb"
        kwargs["width"] = 9
        kwargs["height"] = 2
        kwargs["thickness"] = 70

    # project_variables
    if True:
        pass
    
    # declare parts
    if True:

        part_default = {} 
        part_default["project_name"] = "test" ####### neeeds setting
        part_default["full_shift"] = [0, 0, 0]
        part_default["full_rotations"] = [0, 0, 0]
        
        part = copy.deepcopy(part_default)
        p3 = copy.deepcopy(kwargs)
        p3["thickness"] = 70
        part["kwargs"] = p3
        part["name"] = "base"        
        parts.append(part)

        part = copy.deepcopy(part_default)
        p3 = copy.deepcopy(kwargs)
        p3["thickness"] = 60
        part["kwargs"] = p3
        part["name"] = "base"
        parts.append(part)
        
    #make the parts
    if True:
        for part in parts:
            name = part.get("name", "default")
            if filter in name:
                print(f"making {part['name']}")
                make_scad_generic(part)            
                print(f"done {part['name']}")
            else:
                print(f"skipping {part['name']}")

def get_base(thing, **kwargs):

    width = kwargs.get("width", 9)
    height = kwargs.get("height", 2)
    depth = kwargs.get("thickness", 4)
    prepare_print = kwargs.get("prepare_print", True)

    pos = kwargs.get("pos", [0, 0, 0])
    #pos = copy.deepcopy(pos)
    #pos[2] += -20

    #add plate
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_plate"    
    p3["depth"] = 9
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)
    #add holes
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["width"] = width - 2
    p3["shape"] = f"oobb_holes"
    p3["both_holes"] = True  
    #p3["depth"] = depth
    p3["holes"] = "perimeter"
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)


    #define positions of pegs
    pos_peg_1 = copy.deepcopy(pos)
    pos_peg_1[0] += (width-1)/2*15
    pos_peg_1[1] += (height-1)/2*15

    pos_peg_2 = copy.deepcopy(pos)
    pos_peg_2[0] += -(width-1)/2*15
    pos_peg_2[1] += -(height-1)/2*15

    #add pegs
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_cylinder"
    dep = depth - 9
    p3["depth"] = dep
    p3["radius"] = 14/2
    #p3["m"] = "#"    
    pos1 = copy.deepcopy(pos_peg_1)
    pos1[2] += -dep/2    
    pos2 = copy.deepcopy(pos_peg_2)
    pos2[2] += -dep/2
    poss = []
    poss.append(pos1)
    poss.append(pos2)
    p3["pos"] = poss
    oobb_base.append_full(thing,**p3)
    #add 25mm 3mm deep cylinder to top
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"oobb_cylinder"
        dep2 = 3 + 5
        p3["depth"] = dep2
        p3["radius"] = 25/2
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos_peg_1)
        pos1[2] += -dep + dep2/2 - 5
        pos2 = copy.deepcopy(pos_peg_2)
        pos2[2] += -dep + dep2/2 - 5
        poss = [] 
        poss.append(pos1)
        poss.append(pos2)
        p3["pos"] = poss
        oobb_base.append_full(thing,**p3)
    
    #add nuts for pegs
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_nut"
        p3["radius_name"] = "m6"
        p3["overhang"] = True
        p3["zz"] = "top"
        p3["hole"] = True
        p3["m"] = "#"
        pos1 = copy.deepcopy(pos_peg_1)
        pos1[2] += 9
        pos11 = copy.deepcopy(pos_peg_1)
        pos11[2] += -depth + 9
        pos2 = copy.deepcopy(pos_peg_2)
        pos2[2] += 9
        pos22 = copy.deepcopy(pos_peg_2)
        pos22[2] += -depth + 9
        poss = []
        poss.append(pos1)
        poss.append(pos11)
        poss.append(pos2)
        poss.append(pos22)
        p3["pos"] = poss
        oobb_base.append_full(thing,**p3)

    #add screw to connect
    if True:
        shift_x = 1.5 * 15
        shift_y = 0.5 * 15
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_screw_countersunk"
        p3["radius_name"] = "m3_screw_wood"
        #p3["m"] = "#"
        p3["depth"] = depth
        pos1 = copy.deepcopy(pos)
        pos1[0] += shift_x
        pos1[1] += shift_y
        pos1[2] += 0
        pos2 = copy.deepcopy(pos)
        pos2[0] -= shift_x
        pos2[1] -= shift_y
        pos2[2] += 0
        pos3 = copy.deepcopy(pos)
        pos3[0] += shift_x
        pos3[1] -= shift_y
        pos3[2] += 0
        pos4 = copy.deepcopy(pos)
        pos4[0] -= shift_x
        pos4[1] += shift_y
        pos4[2] += 0
        poss = []
        poss.append(pos1)
        poss.append(pos2)
        poss.append(pos3)
        poss.append(pos4)
        p3["pos"] = poss
        rot = [0,180,0]
        p3["rot"] = rot        
        oobb_base.append_full(thing,**p3)



    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += (width+1)*15
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)
    
###### utilities



def make_scad_generic(part):
    
    # fetching variables
    name = part.get("name", "default")
    project_name = part.get("project_name", "default")
    
    kwargs = part.get("kwargs", {})    
    
    modes = kwargs.get("modes", ["3dpr", "laser", "true"])
    save_type = kwargs.get("save_type", "all")
    overwrite = kwargs.get("overwrite", True)

    kwargs["type"] = f"{project_name}_{name}"

    thing = oobb_base.get_default_thing(**kwargs)
    kwargs.pop("size","")

    #get the part from the function get_{name}"
    try:        
        func = globals()[f"get_{name}"]
        func(thing, **kwargs)
    except:
        get_base(thing, **kwargs)

    for mode in modes:
        depth = thing.get(
            "depth_mm", thing.get("thickness_mm", 3))
        height = thing.get("height_mm", 100)
        layers = depth / 3
        tilediff = height + 10
        start = 1.5
        if layers != 1:
            start = 1.5 - (layers / 2)*3
        if "bunting" in thing:
            start = 0.5
        opsc.opsc_make_object(f'scad_output/{thing["id"]}/{mode}.scad', thing["components"], mode=mode, save_type=save_type, overwrite=overwrite, layers=layers, tilediff=tilediff, start=start)    


if __name__ == '__main__':
    kwargs = {}
    main(**kwargs)