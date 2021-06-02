#include "RecoLocalTracker/SiStripRecHitConverter/interface/SiStripNewRecHitProducer.h"

#include "Geometry/Records/interface/TrackerDigiGeometryRecord.h"
#include "Geometry/TrackerGeometryBuilder/interface/PixelGeomDetUnit.h"
#include "DataFormats/DetId/interface/DetId.h"
#include "DataFormats/Common/interface/Ref.h"
#include "DataFormats/Common/interface/DetSet2RangeMap.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "RecoLocalTracker/Records/interface/TkPixelCPERecord.h"


#include "DataFormats/TrackerRecHit2D/interface/SiStripRecHit2DCollection.h"
#include "DataFormats/TrackerRecHit2D/interface/SiStripMatchedRecHit2DCollection.h"

#include "Geometry/Records/interface/TrackerDigiGeometryRecord.h"
#include "Geometry/CommonDetUnit/interface/GeomDetType.h"
#include "Geometry/CommonDetUnit/interface/GeomDet.h"

#include "Geometry/TrackerGeometryBuilder/interface/PixelGeomDetUnit.h"
#include "Geometry/TrackerGeometryBuilder/interface/PixelGeomDetType.h"
#include "Geometry/TrackerGeometryBuilder/interface/TrackerGeometry.h"
#include "Geometry/CommonTopologies/interface/PixelTopology.h"

#include "RecoLocalTracker/SiPixelRecHits/test/ReadPixelRecHit.h"
#include "DataFormats/TrackerRecHit2D/interface/SiPixelRecHitCollection.h"

#include "DataFormats/DetId/interface/DetId.h"
#include "DataFormats/SiPixelDetId/interface/PXBDetId.h"
#include "DataFormats/SiPixelDetId/interface/PXFDetId.h"
#include "DataFormats/SiPixelDetId/interface/PixelSubdetector.h"


#include <vector>
#include <memory>
#include <string>
#include <iostream>

SiStripNewRecHitProducer::SiStripNewRecHitProducer(const edm::ParameterSet& conf)
:
    conf_(conf),
  inputHits_( conf.getParameter<edm::InputTag>( "inputHits" ) ) {
    consumes< edmNew::DetSetVector<SiStripMatchedRecHit2D> >( inputHits_ );

   produces< edmNew::DetSetVector< SiStripNewRecHit > >();

}

void SiStripNewRecHitProducer::produce(edm::Event& e, const edm::EventSetup& es){
  std::unique_ptr<edmNew::DetSetVector< SiStripNewRecHit > > output(new edmNew::DetSetVector< SiStripNewRecHit > );

  edm::Handle<SiStripMatchedRecHit2DCollection> recHitColl;
  e.getByLabel( inputHits_ , recHitColl);



    const SiStripMatchedRecHit2DCollection* input = recHitColl.product();

  for (SiStripMatchedRecHit2DCollection::const_iterator detunit_iterator = input->begin(); detunit_iterator != input->end(); ++detunit_iterator) {
      unsigned int detid = detunit_iterator->detId();
      edmNew::DetSetVector<SiStripNewRecHit>::FastFiller recHitsOnDetUnit = edmNew::DetSetVector<SiStripNewRecHit>::FastFiller(*output, detid);

      for(SiStripMatchedRecHit2DCollection::DetSet::const_iterator iter=detunit_iterator->begin(), end = detunit_iterator->end(); iter != end; ++iter){//loop on the rechit
	  SiStripMatchedRecHit2D const & rechit=*iter;
          LocalPoint position=rechit.localPosition();
          LocalError error=rechit.localPositionError();
	  std::cout<<"position x = "<<position.x()<<" error = "<<error.xx()<<std::endl;
          SiStripNewRecHit hit = SiStripNewRecHit(position,error);
          recHitsOnDetUnit.push_back(hit);
      }
  }

    e.put(std::move(output));

}
