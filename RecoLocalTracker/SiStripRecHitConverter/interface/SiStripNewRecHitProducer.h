#ifndef RecoLocalTracker_SiStripNewRecHitProducer_h
#define RecoLocalTracker_SiStripNewRecHitProducer_h

#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/stream/EDProducer.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/SiStripNewRecHits/interface/SiStripNewRecHit.h"
#include "DataFormats/SiStripCluster/interface/SiStripCluster.h"
#include "DataFormats/Common/interface/DetSetVectorNew.h"
#include "DataFormats/Common/interface/DetSetVector.h"

#include "RecoLocalTracker/SiPixelRecHits/interface/PixelCPEBase.h"
#include "DataFormats/SiPixelCluster/interface/SiPixelCluster.h"
#include "DataFormats/TrackerRecHit2D/interface/SiPixelRecHitCollection.h"
#ifdef TP_OLD
#include "FWCore/Framework/interface/Handle.h"
#else
#include "DataFormats/Common/interface/Handle.h"
#endif
#include "FWCore/Framework/interface/ESHandle.h"

#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "DataFormats/Common/interface/Handle.h"
#include "FWCore/Framework/interface/EventSetup.h"


#include "FWCore/ParameterSet/interface/ParameterSet.h"


#include <vector>
#include <memory>

class SiStripNewRecHitProducer: public edm::stream::EDProducer<>  {

public:

  explicit SiStripNewRecHitProducer(const edm::ParameterSet& conf);
  void produce(edm::Event&, const edm::EventSetup&) override;

private:

  edm::ParameterSet conf_;
  edm::InputTag inputHits_;

    std::string cpeName_="None";                   // what the user said s/he wanted
    PixelCPEBase const * cpe_=nullptr;                    // What we got (for now, one ptr to base class)
    edm::EDGetTokenT<edmNew::DetSetVector<SiPixelCluster>> tPixelCluster;
    bool m_newCont; // save also in emdNew::DetSetVector

};

DEFINE_FWK_MODULE(SiStripNewRecHitProducer);
#endif
