#---------------------------------------------------------------------------------------------------------------------------------------#
# LOG:                                               							   								  						#
# VERSION					AUTHOR           					DATE 						DESCRIPTION    					  			#
# 1.0.0 					Kareem Hassaan						12 DEC,2021					- Initial Creation				  			#
#---------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------#
# ! Title      	: DIO Configration Project                                                        							  			#
# ! File Name	: DIOConfigrator.py                                                     							  					#
# ! Description : This file Generate te main.c with the configration of the DIO of	Atmega32 Microcontroller    						#
# ! Version  	: Python 3.9.7                                            							  									#
#---------------------------------------------------------------------------------------------------------------------------------------#


#***************************************************************************************************************************************#
#												/* Importing the tkinter GUI library */													#
#***************************************************************************************************************************************#
import tkinter	
from tkinter import *	

#***************************************************************************************************************************************#
#	    										 	/* Main Window Construction GUI */													#
#***************************************************************************************************************************************#				
#Creation a new Empty window
Main_Window = tkinter.Tk()									
#Renaming the Window title
Main_Window.title("DIO Atmega32 Configration")									
#Relocating the window
Main_Window.geometry("1500x550+0+0")						
#Disable resizing the window
Main_Window.resizable(False,False) 							
#changing the window color 
Main_Window.configure(background = "maroon") 

#***************************************************************************************************************************************#
#												         /* Global Variables */      												    #
#***************************************************************************************************************************************#
ColmnRow = 0

while ColmnRow < 9 :
	
	Main_Window.grid_columnconfigure(ColmnRow, minsize = 180) 
	Main_Window.grid_rowconfigure (ColmnRow , minsize = 60)
	ColmnRow += 1

#***************************************************************************************************************************************#
#												      /*PORTA Global Variables */      												    #
#***************************************************************************************************************************************#

#Pin Direction variables
PA_P0_DIR = tkinter.IntVar()
PA_P1_DIR = tkinter.IntVar()
PA_P2_DIR = tkinter.IntVar()
PA_P3_DIR = tkinter.IntVar()
PA_P4_DIR = tkinter.IntVar()
PA_P5_DIR = tkinter.IntVar()
PA_P6_DIR = tkinter.IntVar()
PA_P7_DIR = tkinter.IntVar()

#Pin Value variables
PA_P0_VAL = tkinter.IntVar()
PA_P1_VAL = tkinter.IntVar()
PA_P2_VAL = tkinter.IntVar()
PA_P3_VAL = tkinter.IntVar()
PA_P4_VAL = tkinter.IntVar()
PA_P5_VAL = tkinter.IntVar()
PA_P6_VAL = tkinter.IntVar()
PA_P7_VAL = tkinter.IntVar()

#***************************************************************************************************************************************#
#												      /*PORTB Global Variables */      												    #
#***************************************************************************************************************************************#

#Pin Direction variables
PB_P0_DIR = tkinter.IntVar()
PB_P1_DIR = tkinter.IntVar()
PB_P2_DIR = tkinter.IntVar()
PB_P3_DIR = tkinter.IntVar()
PB_P4_DIR = tkinter.IntVar()
PB_P5_DIR = tkinter.IntVar()
PB_P6_DIR = tkinter.IntVar()
PB_P7_DIR = tkinter.IntVar()
 
#Pin Value variables
PB_P0_VAL = tkinter.IntVar()
PB_P1_VAL = tkinter.IntVar()
PB_P2_VAL = tkinter.IntVar()
PB_P3_VAL = tkinter.IntVar()
PB_P4_VAL = tkinter.IntVar()
PB_P5_VAL = tkinter.IntVar()
PB_P6_VAL = tkinter.IntVar()
PB_P7_VAL = tkinter.IntVar()

#***************************************************************************************************************************************#
#												      /*PORTC Global Variables */      												    #
#***************************************************************************************************************************************#

#Pin Direction variables
PC_P0_DIR = tkinter.IntVar()
PC_P1_DIR = tkinter.IntVar()
PC_P2_DIR = tkinter.IntVar()
PC_P3_DIR = tkinter.IntVar()
PC_P4_DIR = tkinter.IntVar()
PC_P5_DIR = tkinter.IntVar()
PC_P6_DIR = tkinter.IntVar()
PC_P7_DIR = tkinter.IntVar()
 
#Pin Value variables
PC_P0_VAL = tkinter.IntVar()
PC_P1_VAL = tkinter.IntVar()
PC_P2_VAL = tkinter.IntVar()
PC_P3_VAL = tkinter.IntVar()
PC_P4_VAL = tkinter.IntVar()
PC_P5_VAL = tkinter.IntVar()
PC_P6_VAL = tkinter.IntVar()
PC_P7_VAL = tkinter.IntVar()

#***************************************************************************************************************************************#
#												      /*PORTD Global Variables */      												    #
#***************************************************************************************************************************************#

#Pin Direction variables
PD_P0_DIR = tkinter.IntVar()
PD_P1_DIR = tkinter.IntVar()
PD_P2_DIR = tkinter.IntVar()
PD_P3_DIR = tkinter.IntVar()
PD_P4_DIR = tkinter.IntVar()
PD_P5_DIR = tkinter.IntVar()
PD_P6_DIR = tkinter.IntVar()
PD_P7_DIR = tkinter.IntVar()

#Pin Value variables 
PD_P0_VAL = tkinter.IntVar()
PD_P1_VAL = tkinter.IntVar()
PD_P2_VAL = tkinter.IntVar()
PD_P3_VAL = tkinter.IntVar()
PD_P4_VAL = tkinter.IntVar()
PD_P5_VAL = tkinter.IntVar()
PD_P6_VAL = tkinter.IntVar()
PD_P7_VAL = tkinter.IntVar()


#***************************************************************************************************************************************#
#	  								 /* Dict for PORTA Radio Buttons Information in the Main Window */ 									#	
#***************************************************************************************************************************************#

							#--------------------------------------------- PINs DIRECTION -----------------------------------------------#

PORTA_PINS_RADIO_BUTTONS = {'0':{ 'NAME': "  INPUT  "  , 'X_Coordinate': 200, 'Y_Coordinate': 5  , 'variable' : PA_P0_DIR, 'value' : 0},
					        '1':{'NAME': "OUTPUT"      , 'X_Coordinate': 200, 'Y_Coordinate': 30 , 'variable' : PA_P0_DIR, 'value' : 1},
							                                                    
							'2':{'NAME': "  INPUT  "   , 'X_Coordinate': 200, 'Y_Coordinate': 65 , 'variable' : PA_P1_DIR, 'value' : 0},
					        '3':{'NAME': "OUTPUT"      , 'X_Coordinate': 200, 'Y_Coordinate': 90 , 'variable' : PA_P1_DIR, 'value' : 1},
							                                                    
							'4':{'NAME': "  INPUT  "   , 'X_Coordinate': 200, 'Y_Coordinate': 125, 'variable' : PA_P2_DIR, 'value' : 0},
					        '5':{'NAME': "OUTPUT"      , 'X_Coordinate': 200, 'Y_Coordinate': 150, 'variable' : PA_P2_DIR, 'value' : 1},
							                                                    
							'6':{'NAME': "  INPUT  "   , 'X_Coordinate': 200, 'Y_Coordinate': 185, 'variable' : PA_P3_DIR, 'value' : 0},
					        '7':{'NAME': "OUTPUT"      , 'X_Coordinate': 200, 'Y_Coordinate': 210, 'variable' : PA_P3_DIR, 'value' : 1},
							                                                    
							'8':{'NAME': "  INPUT  "   , 'X_Coordinate': 200, 'Y_Coordinate': 245, 'variable' : PA_P4_DIR, 'value' : 0},
					        '9':{'NAME': "OUTPUT"      , 'X_Coordinate': 200, 'Y_Coordinate': 270, 'variable' : PA_P4_DIR, 'value' : 1},
							                                                    
							'10':{ 'NAME': "  INPUT  " , 'X_Coordinate': 200, 'Y_Coordinate': 305, 'variable' : PA_P5_DIR, 'value' : 0},
					        '11':{'NAME': "OUTPUT"     , 'X_Coordinate': 200, 'Y_Coordinate': 330, 'variable' : PA_P5_DIR, 'value' : 1},
							                                                    
							'12':{'NAME': "  INPUT  "  , 'X_Coordinate': 200, 'Y_Coordinate': 365, 'variable' : PA_P6_DIR, 'value' : 0},
					        '13':{'NAME': "OUTPUT"     , 'X_Coordinate': 200, 'Y_Coordinate': 390, 'variable' : PA_P6_DIR, 'value' : 1},
							                                                    
							'14':{'NAME': "  INPUT  "  , 'X_Coordinate': 200, 'Y_Coordinate': 425, 'variable' : PA_P7_DIR, 'value' : 0},
					        '15':{'NAME': "OUTPUT"     , 'X_Coordinate': 200, 'Y_Coordinate': 450, 'variable' : PA_P7_DIR, 'value' : 1},
							
				
							#----------------------------------------------- PINs VALUE -------------------------------------------------#
							
							'16':{'NAME': " HIGH "  , 'X_Coordinate': 273, 'Y_Coordinate': 5  , 'variable' : PA_P0_VAL, 'value' : 1},
					        '17':{'NAME': "  LOW "  , 'X_Coordinate': 273, 'Y_Coordinate': 30 , 'variable' : PA_P0_VAL, 'value' : 0},
							                                               
							'18':{'NAME': " HIGH "  , 'X_Coordinate': 273, 'Y_Coordinate': 65 , 'variable' : PA_P1_VAL, 'value' : 1},
					        '19':{'NAME': "  LOW "  , 'X_Coordinate': 273, 'Y_Coordinate': 90 , 'variable' : PA_P1_VAL, 'value' : 0},
							                                               
							'20':{'NAME': " HIGH "  , 'X_Coordinate': 273, 'Y_Coordinate': 125, 'variable' : PA_P2_VAL, 'value' : 1},
					        '21':{'NAME': "  LOW "  , 'X_Coordinate': 273, 'Y_Coordinate': 150, 'variable' : PA_P2_VAL, 'value' : 0},
							                                               
							'22':{'NAME': " HIGH "  , 'X_Coordinate': 273, 'Y_Coordinate': 185, 'variable' : PA_P3_VAL, 'value' : 1},
					        '23':{'NAME': "  LOW "  , 'X_Coordinate': 273, 'Y_Coordinate': 210, 'variable' : PA_P3_VAL, 'value' : 0},
							                                               
							'24':{'NAME': " HIGH "  , 'X_Coordinate': 273, 'Y_Coordinate': 245, 'variable' : PA_P4_VAL, 'value' : 1},
					        '25':{'NAME': "  LOW "  , 'X_Coordinate': 273, 'Y_Coordinate': 270, 'variable' : PA_P4_VAL, 'value' : 0},
							                                               
							'26':{'NAME': " HIGH "  , 'X_Coordinate': 273, 'Y_Coordinate': 305, 'variable' : PA_P5_VAL, 'value' : 1},
					        '27':{'NAME': "  LOW "  , 'X_Coordinate': 273, 'Y_Coordinate': 330, 'variable' : PA_P5_VAL, 'value' : 0},
							                                               
							'28':{'NAME': " HIGH "  , 'X_Coordinate': 273, 'Y_Coordinate': 365, 'variable' : PA_P6_VAL, 'value' : 1},
					        '29':{'NAME': "  LOW "  , 'X_Coordinate': 273, 'Y_Coordinate': 390, 'variable' : PA_P6_VAL, 'value' : 0},
							                                               
							'30':{'NAME': " HIGH "  , 'X_Coordinate': 273, 'Y_Coordinate': 425, 'variable' : PA_P7_VAL, 'value' : 1},
					        '31':{'NAME': "  LOW "  , 'X_Coordinate': 273, 'Y_Coordinate': 450, 'variable' : PA_P7_VAL, 'value' : 0}}
						
#***************************************************************************************************************************************#
#	  								 /* Dict for PORTB Radio Buttons Information in the Main Window */ 									#	
#***************************************************************************************************************************************#

							#--------------------------------------------- PINs DIRECTION -----------------------------------------------#

PORTB_PINS_RADIO_BUTTONS = {'0':{ 'NAME': "  INPUT  "  , 'X_Coordinate': 565, 'Y_Coordinate': 5  , 'variable' : PB_P0_DIR, 'value' : 0},
					        '1':{'NAME': "OUTPUT"      , 'X_Coordinate': 565, 'Y_Coordinate': 30 , 'variable' : PB_P0_DIR, 'value' : 1},
							                                                                                    
							'2':{'NAME': "  INPUT  "   , 'X_Coordinate': 565, 'Y_Coordinate': 65 , 'variable' : PB_P1_DIR, 'value' : 0},
					        '3':{'NAME': "OUTPUT"      , 'X_Coordinate': 565, 'Y_Coordinate': 90 , 'variable' : PB_P1_DIR, 'value' : 1},
							                                                                                    
							'4':{'NAME': "  INPUT  "   , 'X_Coordinate': 565, 'Y_Coordinate': 125, 'variable' : PB_P2_DIR, 'value' : 0},
					        '5':{'NAME': "OUTPUT"      , 'X_Coordinate': 565, 'Y_Coordinate': 150, 'variable' : PB_P2_DIR, 'value' : 1},
							                                                                                    
							'6':{'NAME': "  INPUT  "   , 'X_Coordinate': 565, 'Y_Coordinate': 185, 'variable' : PB_P3_DIR, 'value' : 0},
					        '7':{'NAME': "OUTPUT"      , 'X_Coordinate': 565, 'Y_Coordinate': 210, 'variable' : PB_P3_DIR, 'value' : 1},
							                                                                                    
							'8':{'NAME': "  INPUT  "   , 'X_Coordinate': 565, 'Y_Coordinate': 245, 'variable' : PB_P4_DIR, 'value' : 0},
					        '9':{'NAME': "OUTPUT"      , 'X_Coordinate': 565, 'Y_Coordinate': 270, 'variable' : PB_P4_DIR, 'value' : 1},
							                                                                                    
							'10':{ 'NAME': "  INPUT  " , 'X_Coordinate': 565, 'Y_Coordinate': 305, 'variable' : PB_P5_DIR, 'value' : 0},
					        '11':{'NAME': "OUTPUT"     , 'X_Coordinate': 565, 'Y_Coordinate': 330, 'variable' : PB_P5_DIR, 'value' : 1},
							                                                                                    
							'12':{'NAME': "  INPUT  "  , 'X_Coordinate': 565, 'Y_Coordinate': 365, 'variable' : PB_P6_DIR, 'value' : 0},
					        '13':{'NAME': "OUTPUT"     , 'X_Coordinate': 565, 'Y_Coordinate': 390, 'variable' : PB_P6_DIR, 'value' : 1},
							                                                                                    
							'14':{'NAME': "  INPUT  "  , 'X_Coordinate': 565, 'Y_Coordinate': 425, 'variable' : PB_P7_DIR, 'value' : 0},
					        '15':{'NAME': "OUTPUT"     , 'X_Coordinate': 565, 'Y_Coordinate': 450, 'variable' : PB_P7_DIR, 'value' : 1},
							
				
							#----------------------------------------------- PINs VALUE -------------------------------------------------#
							
							'16':{'NAME': " HIGH "  , 'X_Coordinate': 638, 'Y_Coordinate': 5  , 'variable' : PB_P0_VAL, 'value' : 1},
					        '17':{'NAME': "  LOW "  , 'X_Coordinate': 638, 'Y_Coordinate': 30 , 'variable' : PB_P0_VAL, 'value' : 0},
							                                                                            
							'18':{'NAME': " HIGH "  , 'X_Coordinate': 638, 'Y_Coordinate': 65 , 'variable' : PB_P1_VAL, 'value' : 1},
					        '19':{'NAME': "  LOW "  , 'X_Coordinate': 638, 'Y_Coordinate': 90 , 'variable' : PB_P1_VAL, 'value' : 0},
							                                                                             
							'20':{'NAME': " HIGH "  , 'X_Coordinate': 638, 'Y_Coordinate': 125, 'variable' : PB_P2_VAL, 'value' : 1},
					        '21':{'NAME': "  LOW "  , 'X_Coordinate': 638, 'Y_Coordinate': 150, 'variable' : PB_P2_VAL, 'value' : 0},
							                                                                             
							'22':{'NAME': " HIGH "  , 'X_Coordinate': 638, 'Y_Coordinate': 185, 'variable' : PB_P3_VAL, 'value' : 1},
					        '23':{'NAME': "  LOW "  , 'X_Coordinate': 638, 'Y_Coordinate': 210, 'variable' : PB_P3_VAL, 'value' : 0},
																											
							'24':{'NAME': " HIGH "  , 'X_Coordinate': 638, 'Y_Coordinate': 245, 'variable' : PB_P4_VAL, 'value' : 1},
					        '25':{'NAME': "  LOW "  , 'X_Coordinate': 638, 'Y_Coordinate': 270, 'variable' : PB_P4_VAL, 'value' : 0},
							                                                                           
							'26':{'NAME': " HIGH "  , 'X_Coordinate': 638, 'Y_Coordinate': 305, 'variable' : PB_P5_VAL, 'value' : 1},
					        '27':{'NAME': "  LOW "  , 'X_Coordinate': 638, 'Y_Coordinate': 330, 'variable' : PB_P5_VAL, 'value' : 0},
							                                                                           
							'28':{'NAME': " HIGH "  , 'X_Coordinate': 638, 'Y_Coordinate': 365, 'variable' : PB_P6_VAL, 'value' : 1},
					        '29':{'NAME': "  LOW "  , 'X_Coordinate': 638, 'Y_Coordinate': 390, 'variable' : PB_P6_VAL, 'value' : 0},
							                                                                           
							'30':{'NAME': " HIGH "  , 'X_Coordinate': 638, 'Y_Coordinate': 425, 'variable' : PB_P7_VAL, 'value' : 1},
					        '31':{'NAME': "  LOW "  , 'X_Coordinate': 638, 'Y_Coordinate': 450, 'variable' : PB_P7_VAL, 'value' : 0}}
													
				    
#***************************************************************************************************************************************#
#	  								 /* Dict for PORTC Radio Buttons Information in the Main Window */ 									#	
#***************************************************************************************************************************************#

							#--------------------------------------------- PINs DIRECTION -----------------------------------------------#

PORTC_PINS_RADIO_BUTTONS = {'0':{'NAME': "  INPUT  "   , 'X_Coordinate': 930, 'Y_Coordinate': 5  , 'variable' : PC_P0_DIR, 'value' : 0},
					        '1':{'NAME': "OUTPUT"      , 'X_Coordinate': 930, 'Y_Coordinate': 30 , 'variable' : PC_P0_DIR, 'value' : 1},
							                                                                                  
							'2':{'NAME': "  INPUT  "   , 'X_Coordinate': 930, 'Y_Coordinate': 65 , 'variable' : PC_P1_DIR, 'value' : 0},
					        '3':{'NAME': "OUTPUT"      , 'X_Coordinate': 930, 'Y_Coordinate': 90 , 'variable' : PC_P1_DIR, 'value' : 1},
							                                                                                 
							'4':{'NAME': "  INPUT  "   , 'X_Coordinate': 930, 'Y_Coordinate': 125, 'variable' : PC_P2_DIR, 'value' : 0},
					        '5':{'NAME': "OUTPUT"      , 'X_Coordinate': 930, 'Y_Coordinate': 150, 'variable' : PC_P2_DIR, 'value' : 1},
							                                                                                  
							'6':{'NAME': "  INPUT  "   , 'X_Coordinate': 930, 'Y_Coordinate': 185, 'variable' : PC_P3_DIR, 'value' : 0},
					        '7':{'NAME': "OUTPUT"      , 'X_Coordinate': 930, 'Y_Coordinate': 210, 'variable' : PC_P3_DIR, 'value' : 1},
							                                                                                  
							'8':{'NAME': "  INPUT  "   , 'X_Coordinate': 930, 'Y_Coordinate': 245, 'variable' : PC_P4_DIR, 'value' : 0},
					        '9':{'NAME': "OUTPUT"      , 'X_Coordinate': 930, 'Y_Coordinate': 270, 'variable' : PC_P4_DIR, 'value' : 1},
							                                                                                  
							'10':{ 'NAME': "  INPUT  " , 'X_Coordinate': 930, 'Y_Coordinate': 305, 'variable' : PC_P5_DIR, 'value' : 0},
					        '11':{'NAME': "OUTPUT"     , 'X_Coordinate': 930, 'Y_Coordinate': 330, 'variable' : PC_P5_DIR, 'value' : 1},
							                                                                                
							'12':{'NAME': "  INPUT  "  , 'X_Coordinate': 930, 'Y_Coordinate': 365, 'variable' : PC_P6_DIR, 'value' : 0},
					        '13':{'NAME': "OUTPUT"     , 'X_Coordinate': 930, 'Y_Coordinate': 390, 'variable' : PC_P6_DIR, 'value' : 1},
							                                                                                 
							'14':{'NAME': "  INPUT  "  , 'X_Coordinate': 930, 'Y_Coordinate': 425, 'variable' : PC_P7_DIR, 'value' : 0},
					        '15':{'NAME': "OUTPUT"     , 'X_Coordinate': 930, 'Y_Coordinate': 450, 'variable' : PC_P7_DIR, 'value' : 1},
							
				
							#----------------------------------------------- PINs VALUE -------------------------------------------------#
							
							'16':{'NAME': " HIGH "  , 'X_Coordinate': 1003, 'Y_Coordinate': 5  , 'variable' : PC_P0_VAL, 'value' : 1},
					        '17':{'NAME': "  LOW "  , 'X_Coordinate': 1003, 'Y_Coordinate': 30 , 'variable' : PC_P0_VAL, 'value' : 0},
							                                                                              
							'18':{'NAME': " HIGH "  , 'X_Coordinate': 1003, 'Y_Coordinate': 65 , 'variable' : PC_P1_VAL, 'value' : 1},
					        '19':{'NAME': "  LOW "  , 'X_Coordinate': 1003, 'Y_Coordinate': 90 , 'variable' : PC_P1_VAL, 'value' : 0},
							                                                                             
							'20':{'NAME': " HIGH "  , 'X_Coordinate': 1003, 'Y_Coordinate': 125, 'variable' : PC_P2_VAL, 'value' : 1},
					        '21':{'NAME': "  LOW "  , 'X_Coordinate': 1003, 'Y_Coordinate': 150, 'variable' : PC_P2_VAL, 'value' : 0},
							                                                                            
							'22':{'NAME': " HIGH "  , 'X_Coordinate': 1003, 'Y_Coordinate': 185, 'variable' : PC_P3_VAL, 'value' : 1},
					        '23':{'NAME': "  LOW "  , 'X_Coordinate': 1003, 'Y_Coordinate': 210, 'variable' : PC_P3_VAL, 'value' : 0},
							                                                                             
							'24':{'NAME': " HIGH "  , 'X_Coordinate': 1003, 'Y_Coordinate': 245, 'variable' : PC_P4_VAL, 'value' : 1},
					        '25':{'NAME': "  LOW "  , 'X_Coordinate': 1003, 'Y_Coordinate': 270, 'variable' : PC_P4_VAL, 'value' : 0},
							                                                                              
							'26':{'NAME': " HIGH "  , 'X_Coordinate': 1003, 'Y_Coordinate': 305, 'variable' : PC_P5_VAL, 'value' : 1},
					        '27':{'NAME': "  LOW "  , 'X_Coordinate': 1003, 'Y_Coordinate': 330, 'variable' : PC_P5_VAL, 'value' : 0},
							                                                                             
							'28':{'NAME': " HIGH "  , 'X_Coordinate': 1003, 'Y_Coordinate': 365, 'variable' : PC_P6_VAL, 'value' : 1},
					        '29':{'NAME': "  LOW "  , 'X_Coordinate': 1003, 'Y_Coordinate': 390, 'variable' : PC_P6_VAL, 'value' : 0},
							                                                                            
							'30':{'NAME': " HIGH "  , 'X_Coordinate': 1003, 'Y_Coordinate': 425, 'variable' : PC_P7_VAL, 'value' : 1},
					        '31':{'NAME': "  LOW "  , 'X_Coordinate': 1003, 'Y_Coordinate': 450, 'variable' : PC_P7_VAL, 'value' : 0}}

#***************************************************************************************************************************************#
#	  								 /* Dict for PORTD Radio Buttons Information in the Main Window */ 									#	
#***************************************************************************************************************************************#
							
							#--------------------------------------------- PINs DIRECTION -----------------------------------------------#
							
PORTD_PINS_RADIO_BUTTONS = {'0':{'NAME': "  INPUT  "   , 'X_Coordinate': 1295, 'Y_Coordinate': 5  , 'variable' : PD_P0_DIR, 'value' : 0},
					        '1':{'NAME': "OUTPUT"      , 'X_Coordinate': 1295, 'Y_Coordinate': 30 , 'variable' : PD_P0_DIR, 'value' : 1},
							                                                                               
							'2':{'NAME': "  INPUT  "   , 'X_Coordinate': 1295, 'Y_Coordinate': 65 , 'variable' : PD_P1_DIR, 'value' : 0},
					        '3':{'NAME': "OUTPUT"      , 'X_Coordinate': 1295, 'Y_Coordinate': 90 , 'variable' : PD_P1_DIR, 'value' : 1},
							                                                                               
							'4':{'NAME': "  INPUT  "   , 'X_Coordinate': 1295, 'Y_Coordinate': 125, 'variable' : PD_P2_DIR, 'value' : 0},
					        '5':{'NAME': "OUTPUT"      , 'X_Coordinate': 1295, 'Y_Coordinate': 150, 'variable' : PD_P2_DIR, 'value' : 1},
							                                                                               
							'6':{'NAME': "  INPUT  "   , 'X_Coordinate': 1295, 'Y_Coordinate': 185, 'variable' : PD_P3_DIR, 'value' : 0},
					        '7':{'NAME': "OUTPUT"      , 'X_Coordinate': 1295, 'Y_Coordinate': 210, 'variable' : PD_P3_DIR, 'value' : 1},
							                                                                               
							'8':{'NAME': "  INPUT  "   , 'X_Coordinate': 1295, 'Y_Coordinate': 245, 'variable' : PD_P4_DIR, 'value' : 0},
					        '9':{'NAME': "OUTPUT"      , 'X_Coordinate': 1295, 'Y_Coordinate': 270, 'variable' : PD_P4_DIR, 'value' : 1},
							                                                                              
							'10':{ 'NAME': "  INPUT  " , 'X_Coordinate': 1295, 'Y_Coordinate': 305, 'variable' : PD_P5_DIR, 'value' : 0},
					        '11':{'NAME': "OUTPUT"     , 'X_Coordinate': 1295, 'Y_Coordinate': 330, 'variable' : PD_P5_DIR, 'value' : 1},
							                                                                            
							'12':{'NAME': "  INPUT  "  , 'X_Coordinate': 1295, 'Y_Coordinate': 365, 'variable' : PD_P6_DIR, 'value' : 0},
					        '13':{'NAME': "OUTPUT"     , 'X_Coordinate': 1295, 'Y_Coordinate': 390, 'variable' : PD_P6_DIR, 'value' : 1},
							                                                                            
							'14':{'NAME': "  INPUT  "  , 'X_Coordinate': 1295, 'Y_Coordinate': 425, 'variable' : PD_P7_DIR, 'value' : 0},
					        '15':{'NAME': "OUTPUT"     , 'X_Coordinate': 1295, 'Y_Coordinate': 450, 'variable' : PD_P7_DIR, 'value' : 1},
							
				
							#----------------------------------------------- PINs VALUE -------------------------------------------------#
							
							'16':{'NAME': " HIGH "  , 'X_Coordinate': 1368, 'Y_Coordinate': 5  , 'variable' : PD_P0_VAL, 'value' : 1},
					        '17':{'NAME': "  LOW "  , 'X_Coordinate': 1368, 'Y_Coordinate': 30 , 'variable' : PD_P0_VAL, 'value' : 0},
							                                                                                
							'18':{'NAME': " HIGH "  , 'X_Coordinate': 1368, 'Y_Coordinate': 65 , 'variable' : PD_P1_VAL, 'value' : 1},
					        '19':{'NAME': "  LOW "  , 'X_Coordinate': 1368, 'Y_Coordinate': 90 , 'variable' : PD_P1_VAL, 'value' : 0},
							                                                                                 
							'20':{'NAME': " HIGH "  , 'X_Coordinate': 1368, 'Y_Coordinate': 125, 'variable' : PD_P2_VAL, 'value' : 1},
					        '21':{'NAME': "  LOW "  , 'X_Coordinate': 1368, 'Y_Coordinate': 150, 'variable' : PD_P2_VAL, 'value' : 0},
		                                                                
							'22':{'NAME': " HIGH "  , 'X_Coordinate': 1368, 'Y_Coordinate': 185, 'variable' : PD_P3_VAL, 'value' : 1},
					        '23':{'NAME': "  LOW "  , 'X_Coordinate': 1368, 'Y_Coordinate': 210, 'variable' : PD_P3_VAL, 'value' : 0},
							                                                                                
							'24':{'NAME': " HIGH "  , 'X_Coordinate': 1368, 'Y_Coordinate': 245, 'variable' : PD_P4_VAL, 'value' : 1},
					        '25':{'NAME': "  LOW "  , 'X_Coordinate': 1368, 'Y_Coordinate': 270, 'variable' : PD_P4_VAL, 'value' : 0},
							                                                                                
							'26':{'NAME': " HIGH "  , 'X_Coordinate': 1368, 'Y_Coordinate': 305, 'variable' : PD_P5_VAL, 'value' : 1},
					        '27':{'NAME': "  LOW "  , 'X_Coordinate': 1368, 'Y_Coordinate': 330, 'variable' : PD_P5_VAL, 'value' : 0},
							                                                                                 
							'28':{'NAME': " HIGH "  , 'X_Coordinate': 1368, 'Y_Coordinate': 365, 'variable' : PD_P6_VAL, 'value' : 1},
					        '29':{'NAME': "  LOW "  , 'X_Coordinate': 1368, 'Y_Coordinate': 390, 'variable' : PD_P6_VAL, 'value' : 0},
							                                                                                 
							'30':{'NAME': " HIGH "  , 'X_Coordinate': 1368, 'Y_Coordinate': 425, 'variable' : PD_P7_VAL, 'value' : 1},
					        '31':{'NAME': "  LOW "  , 'X_Coordinate': 1368, 'Y_Coordinate': 450, 'variable' : PD_P7_VAL, 'value' : 0}}							


							
#***************************************************************************************************************************************#		
#	 									/* Create and Place PORTs Labels in the Main Window */			   								#	
#***************************************************************************************************************************************#

#----------------------------------------------------------------------------------------------------------#
# Function Name		: PORTS_PINS_LABELS																	   #
# Parameters (in)	: None					 											   				   #
# Description		: Function to Create and Place  all PORTs Labels in the Main Window 				   #
#----------------------------------------------------------------------------------------------------------#	
def PORTS_PINS_LABELS():

	Itter = 0
	while (Itter != 32):
		if (Itter < 8):
		
			#Create and Place the label for PORTA PINs in the Main Window
			PORTA_PINX = tkinter.Label(Main_Window, text = "PORTA PIN" + str(Itter) + " : ", width = 15, bg = "white", fg = "black")
			PORTA_PINX.grid(row = Itter, column = 0)
		
		elif ((Itter >= 8) and (Itter < 16)):
		
			#Create and Place the label for PORTB PINs in the Main Window
			PORTB_PINX = tkinter.Label(Main_Window, text = "PORTB PIN" + str(Itter-8) + " : ", width = 15, bg = "white", fg = "black")
			PORTB_PINX.grid(row = (Itter-8), column = 2)
			
		elif ((Itter >= 16) and (Itter < 24)):
		
			#Create and Place the label for PORTC PINs in the Main Window
			PORTC_PINX = tkinter.Label(Main_Window, text = "PORTC PIN" + str(Itter-16) + " : ", width = 15, bg = "white", fg = "black")
			PORTC_PINX.grid(row = (Itter-16), column = 4)
		
		elif ((Itter >= 24) and (Itter < 32)):
		
			#Create and Place the label for PORTD PINs in the Main Window
			PORTD_PINX = tkinter.Label(Main_Window, text = "PORTD PIN" + str(Itter-24) + " : ", width = 15, bg = "white", fg = "black")
			PORTD_PINX.grid(row = (Itter-24), column = 6)
		
		
		Itter += 1

#***************************************************************************************************************************************#		
#	 								/* Create and Place PORTs Radio Buttons in the Main Window */			   							#	
#***************************************************************************************************************************************#		

#----------------------------------------------------------------------------------------------------------#
# Function Name		: PORTA_RADIO_BUTTONS_CREATE														   #
# Parameters (in)	: None					 											   				   #
# Description		: Function to Create and Place PORTA Radio Buttons in the Main Window 				   #
#----------------------------------------------------------------------------------------------------------#
def PORTA_RADIO_BUTTONS_CREATE():

	for i in PORTA_PINS_RADIO_BUTTONS:

		PIN = str(i)
		#Create and Place the Radio Button in the Main Window
		PA_PX_X  = tkinter.Radiobutton(Main_Window,  text = PORTA_PINS_RADIO_BUTTONS[PIN]['NAME'], bg = "maroon", variable = PORTA_PINS_RADIO_BUTTONS[PIN]['variable'], value = PORTA_PINS_RADIO_BUTTONS[PIN]['value'])
		PA_PX_X.place(x = PORTA_PINS_RADIO_BUTTONS[PIN]['X_Coordinate'], y = PORTA_PINS_RADIO_BUTTONS[PIN]['Y_Coordinate'])

#----------------------------------------------------------------------------------------------------------#
# Function Name		: PORTB_RADIO_BUTTONS_CREATE														   #
# Parameters (in)	: None					 											   				   #
# Description		: Function to Create and Place PORTB Radio Buttons in the Main Window 				   #
#----------------------------------------------------------------------------------------------------------#
def PORTB_RADIO_BUTTONS_CREATE():

	for i in PORTB_PINS_RADIO_BUTTONS:

		PIN = str(i)
		#Create and Place the Radio Button in the Main Window
		PA_PX_X  = tkinter.Radiobutton(Main_Window,  text = PORTB_PINS_RADIO_BUTTONS[PIN]['NAME'], bg = "maroon", variable = PORTB_PINS_RADIO_BUTTONS[PIN]['variable'], value = PORTB_PINS_RADIO_BUTTONS[PIN]['value'])
		PA_PX_X.place(x = PORTB_PINS_RADIO_BUTTONS[PIN]['X_Coordinate'], y = PORTB_PINS_RADIO_BUTTONS[PIN]['Y_Coordinate'])

#----------------------------------------------------------------------------------------------------------#
# Function Name		: PORTC_RADIO_BUTTONS_CREATE														   #
# Parameters (in)	: None					 											   				   #
# Description		: Function to Create and Place PORTC Radio Buttons in the Main Window 				   #
#----------------------------------------------------------------------------------------------------------#
def PORTC_RADIO_BUTTONS_CREATE():

	for i in PORTC_PINS_RADIO_BUTTONS:

		PIN = str(i)
		#Create and Place the Radio Button in the Main Window
		PA_PX_X  = tkinter.Radiobutton(Main_Window,  text = PORTC_PINS_RADIO_BUTTONS[PIN]['NAME'], bg = "maroon", variable = PORTC_PINS_RADIO_BUTTONS[PIN]['variable'], value = PORTC_PINS_RADIO_BUTTONS[PIN]['value'])
		PA_PX_X.place(x = PORTC_PINS_RADIO_BUTTONS[PIN]['X_Coordinate'], y = PORTC_PINS_RADIO_BUTTONS[PIN]['Y_Coordinate'])			

#----------------------------------------------------------------------------------------------------------#
# Function Name		: PORTD_RADIO_BUTTONS_CREATE														   #
# Parameters (in)	: None					 											   				   #
# Description		: Function to Create and Place PORTD Radio Buttons in the Main Window 				   #
#----------------------------------------------------------------------------------------------------------#		
def PORTD_RADIO_BUTTONS_CREATE():

	for i in PORTD_PINS_RADIO_BUTTONS:

		PIN = str(i)
		#Create and Place the Radio Button in the Main Window
		PA_PX_X  = tkinter.Radiobutton(Main_Window,  text = PORTD_PINS_RADIO_BUTTONS[PIN]['NAME'], bg = "maroon", variable = PORTD_PINS_RADIO_BUTTONS[PIN]['variable'], value = PORTD_PINS_RADIO_BUTTONS[PIN]['value'])
		PA_PX_X.place(x = PORTD_PINS_RADIO_BUTTONS[PIN]['X_Coordinate'], y = PORTD_PINS_RADIO_BUTTONS[PIN]['Y_Coordinate'])						

#----------------------------------------------------------------------------------------------------------#
# Function Name		: FileGenerationDone														           #
# Parameters (in)	: None					 											   				   #
# Description		: Function to Pop Up a message thet the File.c Generated successfully				   #
#----------------------------------------------------------------------------------------------------------#		
def FileGenerationDone():
	
	#-----------------------------------------------* Creating a new Empty PopUp *----------------------------------------------------#
	
	#Creatin a new Empty window
	PopUpSuccessMsg = tkinter.Toplevel()
	#Renaming the Window title
	PopUpSuccessMsg.title("Confirmation Message")
	#Relocating the window
	PopUpSuccessMsg.geometry("400x100+600+50")
	#changing the window color
	PopUpSuccessMsg.configure(background = "maroon")		
	
	#--------------------------------------------------* Message of the PopUp *-------------------------------------------------------#
	
	#Create and Place the label for the message in Pop Up 
	ErrorAcc = tkinter.Label(PopUpSuccessMsg, text = "DIO_main.c is Generated Successfully", width = 50, bg = "white", fg = "black")
	ErrorAcc.place(x = 25, y = 20)
	#--------------------------------------------------* Buttons of the PopUp *-------------------------------------------------------#
	
	#Create and Place the Button for Exit Pop Up
	Exit = tkinter.Button(PopUpSuccessMsg, text="OK", width = 10 , bg = "white", fg = "black", command = PopUpSuccessMsg.destroy)
	Exit.place(x = 160, y = 60)		
	
#***************************************************************************************************************************************#		
#	 													/* Functions Call */								   							#	
#***************************************************************************************************************************************#
PORTS_PINS_LABELS()
PORTA_RADIO_BUTTONS_CREATE()
PORTB_RADIO_BUTTONS_CREATE()
PORTC_RADIO_BUTTONS_CREATE()
PORTD_RADIO_BUTTONS_CREATE()


#***************************************************************************************************************************************#		
#	 										/* The Main Function that Generate the File.c */				   							#	
#***************************************************************************************************************************************#	

#----------------------------------------------------------------------------------------------------------#
# Function Name		: File_C_Genrator					            									   #
# Parameters (in)	: None					 											   				   #
# Description		: Function to Genrate File.c with the initial configration selected with the main func #
#----------------------------------------------------------------------------------------------------------#
def File_C_Genrator():

	#-------------------------------------- Set DIRECTION REGs Values ---------------------------------------#
	
	DDRA = (PA_P0_DIR.get() << 0)|(PA_P1_DIR.get() << 1)|(PA_P2_DIR.get() << 2)|(PA_P3_DIR.get() << 3)|\
		   (PA_P4_DIR.get() << 4)|(PA_P5_DIR.get() << 5)|(PA_P6_DIR.get() << 6)|(PA_P7_DIR.get() << 7)
	DDRB = (PB_P0_DIR.get() << 0)|(PB_P1_DIR.get() << 1)|(PB_P2_DIR.get() << 2)|(PB_P3_DIR.get() << 3)|\
		   (PB_P4_DIR.get() << 4)|(PB_P5_DIR.get() << 5)|(PB_P6_DIR.get() << 6)|(PB_P7_DIR.get() << 7)
	DDRC = (PC_P0_DIR.get() << 0)|(PC_P1_DIR.get() << 1)|(PC_P2_DIR.get() << 2)|(PC_P3_DIR.get() << 3)|\
		   (PC_P4_DIR.get() << 4)|(PC_P5_DIR.get() << 5)|(PC_P6_DIR.get() << 6)|(PC_P7_DIR.get() << 7)
	DDRD = (PD_P0_DIR.get() << 0)|(PD_P1_DIR.get() << 1)|(PD_P2_DIR.get() << 2)|(PD_P3_DIR.get() << 3)|\
		   (PD_P4_DIR.get() << 4)|(PD_P5_DIR.get() << 5)|(PD_P6_DIR.get() << 6)|(PD_P7_DIR.get() << 7)
	
	#---------------------------------------- Set Value REGs Values -----------------------------------------#
	
	PORTA = (PA_P0_VAL.get() << 0)|(PA_P1_VAL.get() << 1)|(PA_P2_VAL.get() << 2)|(PA_P3_VAL.get() << 3)|\
		    (PA_P4_VAL.get() << 4)|(PA_P5_VAL.get() << 5)|(PA_P6_VAL.get() << 6)|(PA_P7_VAL.get() << 7)
	PORTB = (PB_P0_VAL.get() << 0)|(PB_P1_VAL.get() << 1)|(PB_P2_VAL.get() << 2)|(PB_P3_VAL.get() << 3)|\
		    (PB_P4_VAL.get() << 4)|(PB_P5_VAL.get() << 5)|(PB_P6_VAL.get() << 6)|(PB_P7_VAL.get() << 7)
	PORTC = (PC_P0_VAL.get() << 0)|(PC_P1_VAL.get() << 1)|(PC_P2_VAL.get() << 2)|(PC_P3_VAL.get() << 3)|\
		    (PC_P4_VAL.get() << 4)|(PC_P5_VAL.get() << 5)|(PC_P6_VAL.get() << 6)|(PC_P7_VAL.get() << 7)
	PORTD = (PD_P0_VAL.get() << 0)|(PD_P1_VAL.get() << 1)|(PD_P2_VAL.get() << 2)|(PD_P3_VAL.get() << 3)|\
		    (PD_P4_VAL.get() << 4)|(PD_P5_VAL.get() << 5)|(PD_P6_VAL.get() << 6)|(PD_P7_VAL.get() << 7)
	
	#Open a New file in write mood
	File_C = open("DIO_main.c","w")
	
	#---------------------------------------------------------- File Log Header ------------------------------------------------------------#
	
	File_C.write('''/******************************************************************************************************************\n''')
	File_C.write('''* LOG:                                               														      *\n''')
	File_C.write('''* VERSION				AUTHOR           				DATE 				DESCRIPTION        				  	  *\n''')
	File_C.write('''* 1.0.0 				Kareem Hassaan					XX XXX,20XX			- Initial Creation				  	  *\n''')
	File_C.write('''******************************************************************************************************************/\n''')
	File_C.write('''/******************************************************************************************************************\n''')
	File_C.write('''* ! Title      	: DIO Driver                                                        							  *\n''')
	File_C.write('''* ! File Name	: DIO_main.c                                                         							  *\n''')
	File_C.write('''* ! Description : This file has the main function of the APP		         	       							  *\n''')
	File_C.write('''* ! Compiler  	: GNU AVR cross Compiler                                            							  *\n''')
	File_C.write('''* ! Target 	  	: Atmega32 Micro-Controller                                         							  *\n''')
	File_C.write('''* ! Layer 	  	: MCAL						                                         							  *\n''')
	File_C.write('''******************************************************************************************************************/\n\n''')
	
	#----------------------------------------------------------- Files Inclusion -------------------------------------------------------------#
	
	File_C.write('''/***************************************** Libraries Inclusion ***************************************************/ \n''')
	File_C.write('''#include"../../LIB/STD_TYPES.h" \n''')
	File_C.write('''#include"../../LIB/BIT_MATH.h"\n''')
	File_C.write('''#include"util/delay.h"\n''')
	
	File_C.write('''/**************************************** Self Files Inclusions **************************************************/ \n''')
	File_C.write('''#include"../MCAL/DIO/DIO_intrface.h"''')
	
	#wrriting the main function and oppening its scope
	File_C.write('''\n\nvoid main()\n{\n''')
	
	#------------------------------------------------------ Set Direction Functions ----------------------------------------------------------#
	
	File_C.write("\t/*Setting PortA Directions*/\n")
	File_C.write("\tMDIO_voidSetPortSpecificDirection(PORTA, 0xFF,"+" 0x"+(str(hex(DDRA)[2: ].zfill(2))).upper()+");\n")
	File_C.write("\t/*Setting PortB Directions*/\n")
	File_C.write("\tMDIO_voidSetPortSpecificDirection(PORTB, 0xFF,"+" 0x"+(str(hex(DDRB)[2: ].zfill(2))).upper()+");\n")
	File_C.write("\t/*Setting PortC Directions*/\n")
	File_C.write("\tMDIO_voidSetPortSpecificDirection(PORTC, 0xFF,"+" 0x"+(str(hex(DDRC)[2: ].zfill(2))).upper()+");\n")
	File_C.write("\t/*Setting PortD Directions*/\n")
	File_C.write("\tMDIO_voidSetPortSpecificDirection(PORTD, 0xFF,"+" 0x"+(str(hex(DDRD)[2: ].zfill(2))).upper()+");\n\n")
	
	#-------------------------------------------------------- Set Value Functions ------------------------------------------------------------#
	
	File_C.write("\t/*Setting PortA Values*/\n")
	File_C.write("\tMDIO_voidSetPortSpecificValue(PORTA, 0xFF,"+" 0x"+(str(hex(PORTA)[2: ].zfill(2))).upper()+");\n")
	File_C.write("\t/*Setting PortB Values*/\n")
	File_C.write("\tMDIO_voidSetPortSpecificValue(PORTA, 0xFF,"+" 0x"+(str(hex(PORTB)[2: ].zfill(2))).upper()+");\n")
	File_C.write("\t/*Setting PortC Values*/\n")
	File_C.write("\tMDIO_voidSetPortSpecificValue(PORTA, 0xFF,"+" 0x"+(str(hex(PORTC)[2: ].zfill(2))).upper()+");\n")
	File_C.write("\t/*Setting PortD Values*/\n")
	File_C.write("\tMDIO_voidSetPortSpecificValue(PORTA, 0xFF,"+" 0x"+(str(hex(PORTD)[2: ].zfill(2))).upper()+");\n")
	
	#writing the while(1) Scope
	File_C.write("\n\twhile(1)\n\t{\n\n\t}")
	
	#Closing the main function Scope
	File_C.write("\n}")
	
	#Save and closing the File.c
	File_C.close()
	
	#Pop Up successive Message
	FileGenerationDone()
	

#***************************************************************************************************************************************#		
#	 									/* Create and Place Genrate Button in the Main Window */			   							#	
#***************************************************************************************************************************************#							
#Create and Place the Button for Generate in the main window
Enter = tkinter.Button(Main_Window, text="Generate", width = 30 , bg = "white", fg = "black", command = File_C_Genrator)
Enter.place(x = 610, y = 510)	

#***************************************************************************************************************************************#		
#	 										/* Create the main loop for the main window */												#	
#***************************************************************************************************************************************#

#To keep the window
Main_Window.mainloop() 	

#***************************************************************************************************************************************#	