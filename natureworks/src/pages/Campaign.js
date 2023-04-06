import React from "react";

import CampaignIndividual from "../items/CampaignIndividual";

export default function Campaign() {

  return (
    <div className="campaignList"> 
      <CampaignIndividual date={"6  Mar 2023"} title={"Earth Hour"} description={"Switch off light for 1 hour."} backgroundColor={"#C4F5C3"}/>
      <CampaignIndividual date={"4  Mar 2023"} title={"Zero Waste \n"} description={"Reduce waste, live sustainably."} backgroundColor={"#B4E8C9"}/>
      <CampaignIndividual date={"2  Feb 2023"} title={"Greenify "} description={"Live green, reduce footprint."} backgroundColor={"#E3FEE8"}/>
      <CampaignIndividual date={"3  Apr 2022"} title={"Eco-Friendly"} description={"Transform habits, go eco-friendly."} backgroundColor={"#B7E359"}/>
      <CampaignIndividual date={"23 Mar 2022"} title={"AquaSaver"} description={"Conserve water, reduce waste."} backgroundColor={"#C4F5C3"}/>
      <CampaignIndividual date={"23 Jul 2021"} title={"23 Jun 2023"} description={"23 Jun 2023"} backgroundColor={"#B7E359"}/>

    </div>
  );
}
