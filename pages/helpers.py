#               m  e  r  r  y       c  h  r  i  s  t  m  a  s           
                                                                        
                                                                        
def catch(e, r):                                                        
    def inner(f):                                  #                    
        def wrapper(*args, **kwargs):                                   
            try: f(*args, **kwargs)                                     
            except (e): return r                                        
            return not r                     #                          
        return wrapper                                     #            
    return inner ###########                                            
##################################                                      
def o(func):###################################                         
    def gggg(args):###########################################¹¹¹       
        func(args)#################################     #               
        return args##################                   #               
    return gggg#############       #                    #     *         
#####################              #         *         @##              
###############                  #@@@@                @@###             
############                    #@@@@@@           *   @@###             
#########              *       ##@@@@@@@              @@###             
#               *               ###@@@@                @##              
                                 #####         *        @               
                                                                        
                                                                        
#      h   a   p   p   y     n   e   w        y   e   a   r   !  !  !   