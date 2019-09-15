
#define mbREG_PPM_PON           1
#define mbREG_PPM_1             2
#define mbREG_PPM_2             3
#define mbREG_PPM_3             4
#define mbREG_PPM_4             5
#define mbREG_adc_Vbat          6
#define mbREG_adc_Ibat          7
#define mbREG_adc_Vjet          8
#define mbREG_adc_Ijet          9
#define mbREG_adc_5V            10


#define mbREG_set_mbAddress     0
#define mbREG_set_mbSpeed       1
#define mbREG_GetVersion        2 
#define mbREG_board_control     3
#define mbREG_pid_current_p     4
#define mbREG_pid_current_i     6
#define mbREG_pid_current_d     8
#define mbREG_pid_speed_p       10
#define mbREG_pid_speed_i       12
#define mbREG_pid_speed_d       14
#define mbREG_pid_pos_p         16
#define mbREG_pid_pos_i         18
#define mbREG_pid_pos_d         20
#define mbREG_MaxToSpeed        11 //*2      
#define mbREG_MaxToCurrent      12 //*2     
#define mbREG_MaxToPWM          13 //*2    
#define mbREG_CurrentLimit      28      //Ограничение по току   
#define mbREG_PosCalibration    29      //Коэффициент для самонастройки относительно ноля. Для удобной работы пида
#define mbREG_PosDiv            30      //Делитель положения
#define mbREG_PosMax            31      //Максимальная позиция за которую может выехать серва после чего остановится
#define mbREG_PidSpeedPosFreq   32      //Частота работы пида по скорости и положению 
#define mbREG_PidSpeedMiddle    33      //кол-во усреднений скорости.
#define mbREG_TimeOutLink       34      //таймаут, при отсутствии связи, при которой двигатель будет выключаться
#define mbREG_TimeOutCurrent    35      //таймаут, при превышении тока, при которой двигатель будет выключаться

#define mbREG_command           40      //Регистр команд    
#define mbREG_BridgeOn          41      //включение моста
#define mbREG_SetTask           42      //установка задачи
#define mbREG_SetTimeERR        43      //установка задачи
#define mbREG_SetTimeERRCnt     44      //установка задачи


#define mbREG_GetError          45
#define mbREG_GetEndPoint       46
#define mbREG_GetPosition       47
#define mbREG_GetSpeed          48
#define mbREG_GetCurrent        49
#define mbREG_GetPWM            50
#define mbREG_GetRealPosition   51
#define mbREG_GetLinkTimeOut    52
#define mbREG_GetRPM            53
#define mbREG_LifeTime          54

#define mbREG_GetParrotCur1     55      //попугаие ток, с калибровочным коэффициентом
#define mbREG_current_calibr1   57      //значения калиброки для тока. При отсутствии тока ноль показывало
#define mbREG_GetParrotCur2     56      //попугаие ток, с калибровочным коэффициентом
#define mbREG_current_calibr2   58      //значения калиброки для тока. При отсутствии тока ноль показывало
#define mbREG_AS_error_reg      59      //Регистр ошибки AS405x


#define mbREG_PidSetPosition    31
#define mbREG_PidGetPosition    32
#define mbREG_PidPosOut         33
#define mbREG_PidPositionError  34
#define mbREG_PidPosIterm       35

#define mbREG_PidSetSpeed       36
#define mbREG_PidGetSpeed       37
#define mbREG_PidSpeedOut       38
#define mbREG_PidSpeedError     39
#define mbREG_PidSpeedIterm     40

#define mbREG_PidSetCurrent     41
#define mbREG_PidGetCurrent     42
#define mbREG_PidCurrentOut     43
#define mbREG_PidCurrentError   44
#define mbREG_PidCurrentIterm   45