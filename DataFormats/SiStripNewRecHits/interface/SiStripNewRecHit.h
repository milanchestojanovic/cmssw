#ifndef DATAFORMATS_SISTRIPNEWRECHIT_H
#define DATAFORMATS_SISTRIPNEWRECHIT_H

#include <vector>
#include <numeric>
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "DataFormats/GeometryVector/interface/LocalPoint.h"
#include "DataFormats/GeometrySurface/interface/LocalError.h"

class SiStripNewRecHit  {
public:

  SiStripNewRecHit() {}

  explicit SiStripNewRecHit(const LocalPoint& pos , const LocalError& err):pos_(pos),err_(err) {
  }
//  explicit SiStripNewRecHit(float xpos) {
//  }

  const LocalPoint & localPosition()      const {  return pos_; }
  const LocalError & localPositionError() const {; return err_; }

  LocalPoint pos_;
  LocalError err_;

  //float xpos_;
private:

};
#endif // DATAFORMATS_SISTRIPNEWRECHIT_H
