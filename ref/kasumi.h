/*---------------------------------------------------------
* Kasumi.h
*---------------------------------------------------------*/
#ifndef __KASUMI_H__
#define __KASUMI_H__

typedef unsigned char u8;
typedef unsigned short u16;
//typedef unsigned long u32;
typedef unsigned int u32;

void KeySchedule( u8 *key );
void Kasumi( u8 *data );



#include <stdio.h>

#endif //__KASUMI_H__
