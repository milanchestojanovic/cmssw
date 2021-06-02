#ifndef SISTRIPNEWRECHIT_CLASSES_H
#define SISTRIPNEWRECHIT_CLASSES_H

#include "DataFormats/Common/interface/Wrapper.h"
#include "DataFormats/Common/interface/DetSetVectorNew.h"
#include "DataFormats/Common/interface/Ref.h"
#include "DataFormats/SiStripNewRecHits/interface/SiStripNewRecHit.h"
#include "DataFormats/Common/interface/ContainerMask.h"

namespace DataFormats_SiStripNewRecHit {
  struct dictionary2 {


    edmNew::DetSetVector<SiStripNewRecHit> dsvn;

    edm::Wrapper< SiStripNewRecHit > dummy0;
    edm::Wrapper< std::vector<SiStripNewRecHit>  > dummy1;

    edm::Wrapper< edmNew::DetSetVector<SiStripNewRecHit> > dummy4_bis;

    edm::Wrapper<edm::ContainerMask<edmNew::DetSetVector<SiStripNewRecHit> > > dummy_w_cm1;

    std::vector<edm::Ref<edmNew::DetSetVector<SiStripNewRecHit>,SiStripNewRecHit,edmNew::DetSetVector<SiStripNewRecHit>::FindForDetSetVector> > dummy_v;
    edmNew::DetSetVector<edm::Ref<edmNew::DetSetVector<SiStripNewRecHit>,SiStripNewRecHit,edmNew::DetSetVector<SiStripNewRecHit>::FindForDetSetVector> > dumm_dtvr;
    edm::Wrapper<edmNew::DetSetVector<edm::Ref<edmNew::DetSetVector<SiStripNewRecHit>,SiStripNewRecHit,edmNew::DetSetVector<SiStripNewRecHit>::FindForDetSetVector> > > dumm_dtvr_w;


    edm::Ref<edmNew::DetSetVector<SiStripNewRecHit>, SiStripNewRecHit, edmNew::DetSetVector<SiStripNewRecHit>::FindForDetSetVector > refNew;
  };
}


#endif // SISTRIPNEWRECHIT_CLASSES_H                                                
