/****************************** TRICK HEADER ******************************
PURPOSE: ( Define the QuadRotor vehicle model. )
***************************************************************************/

class QuadRotor
{
  public:
    double mass;                     /**< (kg)   Vehicle mass */
    double position[3];              /**< (m)    Vehicle position */
    double velocity[3];              /**< (m/s)  Vehicle velocity */
    double acceleration[3];          /**< (m/s2) Vehicle acceleration */
};