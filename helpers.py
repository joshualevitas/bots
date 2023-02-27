import random

def robot_body_helper(self,prev_width, prev_depth, prev_height,prev_direction,joint_num,parent):
        depth = random.random() + 0.01 
        width = random.random() * 2 + 0.01 
        height = random.random() + 0.01 
        direction = random.randint(1,3)
        block_name = "Block" + str(joint_num)
        joint_name = parent + "_" + block_name
        random_axis = random.randint(1,20)
        axis = ''
        if random_axis == 1 or random_axis > 6:
            axis = '1 0 0'
        elif random_axis == 2:
            axis = '0 1 0'
        elif random_axis == 3:
            axis = '0 0 1'
        elif random_axis == 4: 
            axis = '1 1 0'
        elif random_axis == 5: 
            axis = '1 0 1'
        elif random_axis == 6:
            axis = '0 1 1'
        type = 'revolute'
        # floating = random.randint(0,10) % 10 == 0
        # if floating: 
            # type = 'floating'
        if direction == 1:
            if prev_direction == 2:
                self.pieces.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
                                            'position':[copy.copy(prev_depth)/2,copy.copy(prev_width)/2,0], 'jointAxis':axis}])
            elif prev_direction == 3:
                self.pieces.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
                                            'position':[0,copy.copy(prev_width)/2,copy.copy(prev_height)/2], 'jointAxis':axis}])
            else:
                self.pieces.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
                                         'position':[0,copy.copy(prev_width)/2,0], 'jointAxis':axis}])  
            self.pieces.append([1,{'name': block_name, 'pos':[0,copy.copy(width)/2,0],'size':[copy.copy(depth) ,copy.copy(width) ,copy.copy(height)]}])
        elif direction == 2:
            if prev_direction == 1:
                self.pieces.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
                                            'position':[copy.copy(prev_depth)/2,copy.copy(prev_width)/2,0], 'jointAxis':axis}])
            elif prev_direction == 3:
                self.pieces.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
                                            'position':[copy.copy(prev_depth)/2,0,copy.copy(prev_height)/2], 'jointAxis':axis}])
            else:
                self.pieces.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
                                            'position':[copy.copy(prev_depth),0,0], 'jointAxis':axis}])                      
            self.pieces.append([1,{'name': block_name, 'pos':[copy.copy(depth)/2,0,0],'size':[copy.copy(depth) ,copy.copy(width) ,copy.copy(height)]}])
        elif direction == 3:
            if prev_direction == 1:
                self.pieces.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
                                            'position':[0,copy.copy(prev_width)/2,copy.copy(prev_height)/2], 'jointAxis':axis}])
            elif prev_direction == 2:
                self.pieces.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
                                            'position':[copy.copy(prev_depth)/2,0,copy.copy(prev_height)/2], 'jointAxis':axis}])
            else: 
                self.pieces.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
                                        'position':[0,0,copy.copy(prev_height)], 'jointAxis':axis}])
            self.pieces.append([1,{'name': block_name, 'pos':[0,0,copy.copy(height)/2],'size':[copy.copy(depth) ,copy.copy(width) ,copy.copy(height)]}])                
        else:
            print(direction)
            exit()
    
        parent = block_name
        prev_width = width
        prev_depth = depth
        prev_height = height
        prev_direction = direction
        joint_num +=1
        self.unclaimedJoints.append(joint_name)
        self.lastlinks.append([prev_width, prev_depth, prev_height,prev_direction,joint_num,parent])