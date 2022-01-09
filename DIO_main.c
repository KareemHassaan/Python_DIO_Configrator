/******************************************************************************************************************
* LOG:                                               														      *
* VERSION				AUTHOR           				DATE 				DESCRIPTION        				  	  *
* 1.0.0 				Kareem Hassaan					XX XXX,20XX			- Initial Creation				  	  *
******************************************************************************************************************/
/******************************************************************************************************************
* ! Title      	: DIO Driver                                                        							  *
* ! File Name	: DIO_main.c                                                         							  *
* ! Description : This file has the main function of the APP		         	       							  *
* ! Compiler  	: GNU AVR cross Compiler                                            							  *
* ! Target 	  	: Atmega32 Micro-Controller                                         							  *
* ! Layer 	  	: MCAL						                                         							  *
******************************************************************************************************************/

/***************************************** Libraries Inclusion ***************************************************/ 
#include"../../LIB/STD_TYPES.h" 
#include"../../LIB/BIT_MATH.h"
#include"util/delay.h"
/**************************************** Self Files Inclusions **************************************************/ 
#include"../MCAL/DIO/DIO_intrface.h"

void main()
{
	/*Setting PortA Directions*/
	MDIO_voidSetPortSpecificDirection(PORTA, 0xFF, 0x00);
	/*Setting PortB Directions*/
	MDIO_voidSetPortSpecificDirection(PORTB, 0xFF, 0x00);
	/*Setting PortC Directions*/
	MDIO_voidSetPortSpecificDirection(PORTC, 0xFF, 0x00);
	/*Setting PortD Directions*/
	MDIO_voidSetPortSpecificDirection(PORTD, 0xFF, 0x00);

	/*Setting PortA Values*/
	MDIO_voidSetPortSpecificValue(PORTA, 0xFF, 0x00);
	/*Setting PortB Values*/
	MDIO_voidSetPortSpecificValue(PORTA, 0xFF, 0x00);
	/*Setting PortC Values*/
	MDIO_voidSetPortSpecificValue(PORTA, 0xFF, 0x00);
	/*Setting PortD Values*/
	MDIO_voidSetPortSpecificValue(PORTA, 0xFF, 0x00);

	while(1)
	{

	}
}