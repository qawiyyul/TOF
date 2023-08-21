
/**
  ******************************************************************************
  * @file    53l7a1_conf.h
  * @author  IMG SW Application Team
  * @brief   This file contains definitions for the ToF components bus interfaces
  *          when using the X-NUCLEO-53L7A1 expansion board
  ******************************************************************************
  * @attention
  *
  * Copyright (c) 2022 STMicroelectronics.
  * All rights reserved.
  *
  * This software is licensed under terms that can be found in the LICENSE file
  * in the root directory of this software component.
  * If no LICENSE file comes with this software, it is provided AS-IS.
  *
  ******************************************************************************
  */

#include "stm32g4xx_hal.h"
#include "stm32g4xx_nucleo_bus.h"
#include "stm32g4xx_nucleo_errno.h"

/* Define to prevent recursive inclusion -------------------------------------*/
#ifndef VL53L7A1_CONF_H
#define VL53L7A1_CONF_H

#ifdef __cplusplus
extern "C" {
#endif

/* USER CODE BEGIN 1 */

/* USER CODE END 1 */

/*
 * the 53L7A1 BSP driver uses this symbol to allocate a structure for each device
 * if you are only using the on-board sensor without break-out boards
 * change its to (1U) in order to save space in RAM memory
 */
#define RANGING_SENSOR_INSTANCES_NBR    (3U)

#define VL53L7A1_hi2c                   (hi2c1)

#define VL53L7A1_I2C_SCL_GPIO_PORT      BUS_I2C1_SCL_GPIO_PORT
#define VL53L7A1_I2C_SCL_GPIO_PIN       BUS_I2C1_SCL_GPIO_PIN
#define VL53L7A1_I2C_SDA_GPIO_PORT      BUS_I2C1_SDA_GPIO_PORT
#define VL53L7A1_I2C_SDA_GPIO_PIN       BUS_I2C1_SDA_GPIO_PIN

#define VL53L7A1_I2C_Init               BSP_I2C1_Init
#define VL53L7A1_I2C_DeInit             BSP_I2C1_DeInit
#define VL53L7A1_I2C_WriteReg           BSP_I2C1_WriteReg16
#define VL53L7A1_I2C_ReadReg            BSP_I2C1_ReadReg16
#define VL53L7A1_GetTick                BSP_GetTick

#ifdef __cplusplus
}
#endif

#endif /* VL53L7A1_CONF_H*/
