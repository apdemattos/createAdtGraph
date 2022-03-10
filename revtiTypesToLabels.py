# Map Revit Families to their corresponding DTDL Model
revitFamiliesToDtDlModel = {
    #Architectural
    'HSS-Hollow Structural Section': 'BuildingComponent:Structural:StructuralBeam',
    'Concrete-Square-Column': 'BuildingComponent:Structural:StructuralBeam',
    'HSS-Hollow Structural Section-Column': 'BuildingComponent:Structural:StructuralColumn',
    'Ceilings': 'BuildingComponent:Architectural:Ceiling',
    'Floors': 'BuildingComponent:Architectural:Floor',
    'Walls': 'BuildingComponent:Architectural:Wall',
    'Fascias': 'BuildingComponent:Architectural:Facade',
    'Roofs': 'BuildingComponent:Architectural:Roof',

    # Mechanical
    'Rectangular Duct': 'Asset:DistributionAsset:HVACDuct:HVACRectangularDuct', 
    'Round Duct': 'Asset:DistributionAsset:HVACDuct:HVACRoundDuct',
    'Floor Drain - Round': 'Asset:Equipment:Plumbing:Drain:FloorDrain',
    'Lavatory - Wall Mounted': 'Asset:Equipment:Plumbing:PlumbingFixture:Sink',
    'RainwaterTank': 'Asset:Equipment:HVAC:Tank:HVACTank',
    'Rectangular Tap - Beveled': 'Asset:DistributionAsset:DistributionConnector:HVACDuctFitting:HVACDuctFitting',
    'Rectangular Elbow - Mitered': 'Asset:DistributionAsset:DistributionConnector:HVACDuctFitting:HVACDuctFitting',
    'Rectangular Elbow - Radius': 'Asset:DistributionAsset:DistributionConnector:HVACDuctFitting:HVACDuctFitting',
    'Rectangular Transition - Angle': 'Asset:DistributionAsset:DistributionConnector:HVACDuctFitting:HVACDuctFitting',
    'Rectangular Endcap': 'Asset:DistributionAsset:DistributionConnector:HVACDuctFitting:HVACDuctFitting',
    'Rectangular Tap - Beveled': 'Asset:DistributionAsset:DistributionConnector:HVACDuctFitting:HVACDuctFitting',
    'Rectangular Sharp Throat Radius Heel Elbow - DTL': 'Asset:DistributionAsset:DistributionConnector:HVACDuctFitting:HVACDuctFitting',
    'Rectangular to Round Transition - Angle': 'Asset:DistributionAsset:DistributionConnector:HVACDuctFitting:HVACDuctFitting',
    'Round Takeoff': 'Asset:DistributionAsset:DistributionConnector:HVACDuctFitting:HVACDuctFitting',
    'Round to Rectangular Transition - Angle': 'Asset:DistributionAsset:DistributionConnector:HVACDuctFitting:HVACDuctFitting',
    'Rectangular Wye - Smooth Radius': 'Asset:DistributionAsset:DistributionConnector:HVACDuctFitting:HVACDuctFitting',
    'SA_Rectangular Mitered Elbow': 'Asset:DistributionAsset:DistributionConnector:HVACDuctFitting:HVACDuctFitting',
    'Round Takeoff Conical': 'Asset:DistributionAsset:DistributionConnector:HVACDuctFitting:HVACDuctFitting',
    'Round Elbow': 'Asset:DistributionAsset:DistributionConnector:HVACDuctFitting:HVACDuctFitting',
    'Rectangular Takeoff': 'Asset:DistributionAsset:DistributionConnector:HVACDuctFitting:HVACDuctFitting',
    'SA_Open End Duct with Wire Mesh': 'Asset:DistributionAsset:DistributionConnector:HVACDuctFitting:HVACDuctFitting',
    'Round Transition - Angle': 'Asset:DistributionAsset:DistributionConnector:HVACDuctFitting:HVACDuctFitting',
    'SA_Round Taps - Conical Takeoff': 'Asset:DistributionAsset:DistributionConnector:HVACDuctFitting:HVACDuctFitting',
    'SA_Rectangular Elbow - Mitered': 'Asset:DistributionAsset:DistributionConnector:HVACDuctFitting:HVACDuctFitting',
    'Rectangular to Round Transition - Angle': 'Asset:DistributionAsset:DistributionConnector:HVACDuctFitting:HVACDuctFitting',
    'SA_Rectangular Tee - Mitered': 'Asset:DistributionAsset:DistributionConnector:HVACDuctFitting:HVACDuctFitting',
    'SA_Rectangular to Round Transition - Length': 'Asset:DistributionAsset:DistributionConnector:HVACDuctFitting:HVACDuctFitting',
    'SA_Round Elbow': 'Asset:DistributionAsset:DistributionConnector:HVACDuctFitting:HVACDuctFitting',
    'SA_Rectangular Tap - Beveled': 'Asset:DistributionAsset:DistributionConnector:HVACDuctFitting:HVACDuctFitting',
    'SA_Rectangular Tap - Takeoff': 'Asset:DistributionAsset:DistributionConnector:HVACDuctFitting:HVACDuctFitting',
    'Round Transition - Length': 'Asset:DistributionAsset:DistributionConnector:HVACDuctFitting:HVACDuctFitting',
    'SA_Open End Duct with Wire Mesh Screen - Return Air ': 'Asset:DistributionAsset:DistributionConnector:HVACDuctFitting:HVACDuctFitting',
    'SA_Round Transition - Length': 'Asset:DistributionAsset:DistributionConnector:HVACDuctFitting:HVACDuctFitting',
    'Rectangular Tee': 'Asset:DistributionAsset:DistributionConnector:HVACDuctFitting:HVACDuctFitting',
    'Rectangular Tee - Reducing': 'Asset:DistributionAsset:DistributionConnector:HVACDuctFitting:HVACDuctFitting',
    'Rectangular Cross': 'Asset:DistributionAsset:DistributionConnector:HVACDuctFitting:HVACDuctFitting',
    'Round Takeoff - Conical': 'Asset:DistributionAsset:DistributionConnector:HVACDuctFitting:HVACDuctFitting',
    'Round Transition - Angle': 'Asset:DistributionAsset:DistributionConnector:HVACDuctFitting:HVACDuctFitting',
    'Rectangular Transition Pants - DTL': 'Asset:DistributionAsset:DistributionConnector:HVACDuctFitting:HVACDuctFitting',
    'Rectangular Tap - Pyramidal': 'Asset:DistributionAsset:DistributionConnector:HVACDuctFitting:HVACDuctFitting',
    'Pipe Types': 'Asset:DistributionAsset:Pipe',
    'Transition - Generic': 'Asset:DistributionAsset:DistributionConnector:PipeFitting',
    'Elbow - Generic': 'Asset:DistributionAsset:DistributionConnector:PipeFitting:PipeFittingElbow',
    'Tee - Generic': 'Asset:DistributionAsset:DistributionConnector:PipeFitting:PipeFittingTee',
    'Pipe Spud': 'Asset:DistributionAsset:DistributionConnector:PipeFitting',
    'Coupling - Generic': 'Asset:DistributionAsset:DistributionConnector:PipeFitting:PipeFittingCoupling',
    'Climate Master - TS Series': 'Asset:Equipment:HVAC:AirHandlingUnit',
    'Krueger LMHS-HWC': 'Asset:Equipment:HVAC:TerminalUnit:VAVBox:VAVBoxReheat',
    'Krueger LMHS': 'Asset:Equipment:HVAC:TerminalUnit:VAVBox',
    'Cabinet Fan-BCF': 'Asset:Equipment:HVAC:Fan:HVACFan',
    'Unit Heater - Cabinet': 'Asset:Equipment:HVAC:UnitHeater',
    'Pool Unit': 'Asset:Equipment:HVAC:AirHandlingUnit',
    'AHU 1,3,7': 'Asset:Equipment:HVAC:AirHandlingUnit',
    'Air_Handling_Unit-Aaon-RNA-V-AC-GAS': 'Asset:Equipment:HVAC:AirHandlingUnit',
    'AHU': 'Asset:Equipment:HVAC:AirHandlingUnit',
    'BG Base Mounted Centrifugal Pump Series 1510-5': 'Asset:Equipment:HVAC:Pump:HVACPump',
    'Expansion Tank - Freestanding - Vertical': 'Asset:Equipment:HVAC:Tank:HVACTank',
    'BAC - Cooling Tower': 'Asset:Equipment:HVAC:CoolingTower',
    'Greenheck Sidewall Exhaust': 'Asset:Equipment:HVAC:Fan:ExhaustFan',
    'DOAS 1,2,8': 'Asset:Equipment:HVAC:AirHandlingUnit:DedicatedOutdoorAirSystem',
    'DOAS': 'Asset:Equipment:HVAC:AirHandlingUnit:DedicatedOutdoorAirSystem',
    'AHU 2,5': 'Asset:Equipment:HVAC:AirHandlingUnit',
    'Heat_Recovery_Unit-VRV_IV-Daikin-REYQ_72-168_TATJU-TAYDU': 'Asset:Equipment:HVAC',
    'HVAC-Inffuser-Dadanco-IDS60i_1': 'Asset:DistributionAsset:DistributionConnector:HVACDuctFitting:HVACDuctFitting',
    'Air_Conditioner-Daikin-FXFQ_TVJU': 'Asset:Equipment:HVAC:TerminalUnit:FanCoilUnit',
    'Air_Conditioner-VRV_IV-Daikin-FXAQ_PVJU': 'Asset:Equipment:HVAC:TerminalUnit:FanCoilUnit',
    'Branch_Selector-Single_Port-Daikin-BSQ': 'Asset:Equipment:HVAC',
    'Ceiling_Suspended_Unit-SkyAir-Daikin-FHQ_PVJU': 'Asset:Equipment:HVAC:TerminalUnit:FanCoilUnit',
    'AMERICAN ALDES - SD': 'Asset:DistributionAsset:DistributionConnector:HVACDuctFitting:HVACDuctFitting',
    'Cooling_Unit-Sky_Air-Daikin-RZR_PVJU': 'Asset:Equipment:HVAC:TerminalUnit:FanCoilUnit',
    'Air_Handling_Unit- Daikin - DPS012A': 'Asset:Equipment:HVAC:AirHandlingUnit',
    'Unit_Heater-Gas-Modine-PDP Unit-Propeller': 'Asset:Equipment:HVAC:UnitHeater',
    'Titus 300, 301, Louvered Supply Grilles Revit 2015 V5': 'Asset:Equipment:HVAC:TerminalUnit',
    'Titus 300R-HD,301R-HD - Heavy Duty Louvered Return Grille, Face Mount, Revit 2015 R1.0': 'Asset:Equipment:HVAC:TerminalUnit',
    'Titus 300, 301, Louvered Return Grilles Revit 2015 V5': 'Asset:Equipment:HVAC:TerminalUnit',
    'Ceiling_Diffusers-RID-Size_12-Price_Industries': 'Asset:Equipment:HVAC:TerminalUnit',
    'Titus-Linear_Supply_Diffuser-ML_With_MP': 'Asset:Equipment:HVAC:TerminalUnit',
    'Fire Damper - Rectangular - Simple': 'Asset:Equipment:HVAC:DamperEquipment:HVACDamper',
    'Control Damper - Manual - Rectangular': 'Asset:Equipment:HVAC:DamperEquipment:HVACDamper',
    'CUBE_LOD200_AllSizes': 'Asset:Equipment:HVAC:Fan:ExhaustFan',
    'Greenheck Rooftop Ventilator': 'Asset:Equipment:HVAC:Fan:ExhaustFan',
    'CaptiveAire Rooftop Ventilator': 'Asset:Equipment:HVAC:Fan:ExhaustFan',
    'G_LOD200_AllSizes': 'Asset:Equipment:HVAC:Fan:ExhaustFan',
    'HVAC-Inffuser-Dadanco-IDS60i_1': 'Asset:DistributionAsset:DistributionConnector:HVACDuctFitting:HVACDuctFitting',
    'RooftopVentilator 10,25': 'Asset:Equipment:HVAC:Fan:ExhaustFan',
    'RooftopVentilator': 'Asset:Equipment:HVAC:Fan:ExhaustFan',
    'MAU': 'Asset:Equipment:HVAC:AirHandlingUnit:MakeupAirUnit',
    'Horizontal FCU': 'Asset:Equipment:HVAC:TerminalUnit:FanCoilUnit',
    'Unit Heater': 'Asset:Equipment:HVAC:UnitHeater',
    'Refrigeration Unit': 'Asset:Equipment:Foodservice:FoodStorage:Refrigeration:RefrigerationEquipment',
    'FCU Stair': 'Asset:Equipment:HVAC:TerminalUnit:FanCoilUnit',
    'Cabinet Fan-BDF': 'Asset:Equipment:HVAC:Fan:ReturnFan',
    'InlineTubeFan-Horiz': 'Asset:Equipment:HVAC:Fan:ReturnFan',
    'Chiller': 'Asset:Equipment:HVAC:Chiller',
    'Heat Exchanger': 'Asset:Equipment:HVAC:HeatExchanger',
    'WWHP': 'Asset:Equipment:HVAC:Pump:HVACPump',
    'FCU IT': 'Asset:Equipment:HVAC:TerminalUnit:FanCoilUnit',
    'BG Base Mounted Centrifugal Pump Series 1510-4': 'Asset:Equipment:HVAC:Pump:HVACPump',
    'Bio Tank': 'Asset:Equipment:HVAC:Tank:HVACTank',
    'BG_In-Line Mounted Pump_Series 80-1.5x1.5xX': 'Asset:Equipment:HVAC:Tank:HVACTank',
    'CeilingFan': 'Asset:Equipment:HVAC:Fan:CeilingFan',
    'BAS Panel': 'Asset:Equipment:Security:AccessControl:AccessControlPanel',
    'Bypass Feeder': 'Asset',
    'ACC': 'Asset',
    'Titus PAS (CD)': 'Asset:DistributionAsset',
    'Titus 350RL (RG)': 'Asset:DistributionAsset',
    'Titus PAR (RG)': 'Asset:DistributionAsset',
    'Titus 350RL (EG)': 'Asset:DistributionAsset',
    'Titus 301RL (SG)': 'Asset:DistributionAsset',
    'Titus ML-39 (LD)': 'Asset:DistributionAsset',
    'Titus TMR (RD)': 'Asset:DistributionAsset',
    'Titus PAS (DL)': 'Asset:DistributionAsset',
    'Titus 350FL (RG)': 'Asset:DistributionAsset',
    'Louver - Extruded': 'Asset:DistributionAsset',
    'Flex Duct Round': 'Asset:DistributionAsset:HVACDuct:HVACRoundDuct', 
    'Flex Duct Rectangular': 'Asset:DistributionAsset:HVACDuct:HVACRectangularDuct',
    'Control Damper - Automatic - Rectangular': 'Asset:Equipment:HVAC:DamperEquipment:HVACDamper',
    'Air Separator with Strainer - Tangential - 3-14 Inch - Flanged': 'Asset:DistributionAsset:Pipe',
    '3 Way Valve - 0.75-4 Inch': 'Asset:DistributionAsset:Pipe',
    'Motor Control Valve - 0.5-2 Inch': 'Asset:DistributionAsset:Pipe',
    'Flex Pipe Round': 'Asset:DistributionAsset:Pipe',

    # Electrical 
    'SA_Wall Strobe': 'Asset:Equipment:FireProtection:FireAlarm:FireAlarmNotificationAppliance:FireAlarmStrobe',
    'SA_Manual Pull Station': 'Asset:Equipment:FireProtection:FireAlarm:FireAlarmInitiatingDevice:FireAlarmPullStation',
    'SA_Ceiling Speaker': 'Asset:Equipment:FireProtection:FireAlarm:FireAlarmNotificationAppliance:FireAlarmSpeaker',
    'SA_Wall Strobe & Speaker(AV)': 'Asset:Equipment:FireProtection:FireAlarm:FireAlarmNotificationAppliance:FireAlarmSpeakerStrobe',
    'SA_Smoke Detector': 'Asset:Equipment:FireProtection:FireAlarm:FireAlarmInitiatingDevice:FireDetector:SmokeDetector',
    'SA_Wall Heat Detector': 'Asset:Equipment:FireProtection:FireAlarm:FireAlarmInitiatingDevice:FireDetector:HeatDetector',
    'SA_Wall Smoke Detector': 'Asset:Equipment:FireProtection:FireAlarm:FireAlarmInitiatingDevice:FireDetector:SmokeDetector',
    'SA_Wall Strobe & Speaker(AV) MP': 'Asset:Equipment:FireProtection:FireAlarm:FireAlarmNotificationAppliance:FireAlarmSpeakerStrobe',
    'SA_Wall Strobe MP': 'Asset:Equipment:FireProtection:FireAlarm:FireAlarmNotificationAppliance:FireAlarmStrobe',
    'SA_Ceiling Strobe & Speaker': 'Asset:Equipment:FireProtection:FireAlarm:FireAlarmNotificationAppliance:FireAlarmSpeakerStrobe',
    'SA_Heat Detector': 'Asset:Equipment:FireProtection:FireAlarm:FireAlarmInitiatingDevice:FireDetector:HeatDetector',
    'SA_Ceiling Strobe': 'Asset:Equipment:FireProtection:FireAlarm:FireAlarmNotificationAppliance:FireAlarmStrobe',
    'SA_FATC': 'Asset:Equipment:FireProtection:FireAlarm:FireAlarmControlPanel',
    'SA_FAAP': 'Asset:Equipment:FireProtection:FireAlarm:FireAlarmControlPanel',
    'SA_ Duct Smoke Detector': 'Asset:Equipment:FireProtection:FireAlarm:FireAlarmInitiatingDevice:FireDetector:SmokeDetector',
    'SA_FACP': 'Asset:Equipment:FireProtection:FireAlarm:FireAlarmControlPanel',
    'SA_Ceiling Occupancy Sensor - LUTRON': 'Asset:Equipment:Lighting:LightingEquipment',
    'Wall Occupancy Sensor - Dual Relay': 'Asset:Equipment:Lighting:LightingEquipment',
    'Lighting Switches': 'Asset:Equipment:Lighting:LightingEquipment',
    'SA_Ceiling Occupancy Sensor - Dual Relay - Regular Voltage': 'Asset:Equipment:Lighting:LightingEquipment',
    'Sensor_Interface-Lutron-QSM24WC': 'Asset:Equipment:Lighting:LightingEquipment',
    'Weather Proof Switch': 'Asset:Equipment:Lighting:LightingEquipment',
    'Daylight_Sensor_-_Lutron_-_EcoSystem_-_EC-DIR-WH': 'Asset:Equipment:Lighting:LightingEquipment',
    'SA_Wall Exit without arrow.0001': 'Asset:Equipment:Lighting:Safety:ExitSign',
    'SA_Exit dual arrow': 'Asset:Equipment:Lighting:Safety:ExitSign',
    'SA_Exit without arrow': 'Asset:Equipment:Lighting:Safety:ExitSign',
    'SA_Exit RU arrow': 'Asset:Equipment:Lighting:Safety:ExitSign',
    'SA_Wall Exit RU arrow': 'Asset:Equipment:Lighting:Safety:ExitSign',
    'SA_Exit LU arrow': 'Asset:Equipment:Lighting:Safety:ExitSign',
    'SA_Exit dual arrow(Pendant)': 'Asset:Equipment:Lighting:Safety:ExitSign',
    'SA_Wall Exit LU arrow': 'Asset:Equipment:Lighting:Safety:ExitSign',
    'SA_Exit 2way arrow': 'Asset:Equipment:Lighting:Safety:ExitSign',
    'SA_Exit dual 2W arrow(Pendant)': 'Asset:Equipment:Lighting:Safety:ExitSign',
    'SA_Exit without arrow(Pendant)': 'Asset:Equipment:Lighting:Safety:ExitSign',
    'Lighting Type R- Downlight - PENDANT Can': 'Asset:Equipment:Lighting:LightingEquipment',
    'Lighting Type G- Downlight - Recessed Can': 'Asset:Equipment:Lighting:LightingEquipment',
    'Lighting Type A - Suspended Linear': 'Asset:Equipment:Lighting:LightingEquipment',
    'Lighting Type F - KITCHEN - 2x4': 'Asset:Equipment:Lighting:LightingEquipment',
    'Lighting Type I - ARMORY (decorative)': 'Asset:Equipment:Lighting:LightingEquipment',
    'Lighting Type M - corridor': 'Asset:Equipment:Lighting:LightingEquipment',
    'Lighting Type C - Troffer - 2x2 Direct Indirect': 'Asset:Equipment:Lighting:LightingEquipment',
    'Lighting Type U- ceiling mtd': 'Asset:Equipment:Lighting:LightingEquipment',
    'Lighting Type K - recessed': 'Asset:Equipment:Lighting:LightingEquipment',
    'Lighting Type N - POOL (NOT HOSTED)': 'Asset:Equipment:Lighting:LightingEquipment',
    'Lighting Type H - Perimeter Walwash (Toilet Rm)': 'Asset:Equipment:Lighting:LightingEquipment',
    'Lighting Type L - CoveLight': 'Asset:Equipment:Lighting:LightingEquipment',
    'Lighting Type E- wall mtd': 'Asset:Equipment:Lighting:LightingEquipment',
    'Lighting Type S - Parking': 'Asset:Equipment:Lighting:LightingEquipment',
    'Lighting Type P - GYM': 'Asset:Equipment:Lighting:LightingEquipment',
    'Lighting Type M - slope': 'Asset:Equipment:Lighting:LightingEquipment',
    'Lighting Type H - slope': 'Asset:Equipment:Lighting:LightingEquipment',
    'Lighting Type V - POOL EM': 'Asset:Equipment:Lighting:LightingEquipment',
    'Lighting Type V- ceiling mtd': 'Asset:Equipment:Lighting:LightingEquipment',
    'Lighting Type U- ceiling mtd1': 'Asset:Equipment:Lighting:LightingEquipment',
    'Lighting Type B - Armory': 'Asset:Equipment:Lighting:LightingEquipment',
    'X1': 'Asset:Equipment:Lighting:LightingEquipment',
    'Lighting Type W - Perimeter (media center tower)': 'Asset:Equipment:Lighting:LightingEquipment',
    'X5': 'Asset:Equipment:Lighting:LightingEquipment',
    'X6': 'Asset:Equipment:Lighting:LightingEquipment',
    'X4': 'Asset:Equipment:Lighting:LightingEquipment',
    'SA_Duplex Receptacle': 'Asset:Equipment:Electrical:ElectricalDistribution:ElectricalWiringDevice:ElectricalReceptacle',
    'SA_Quad IG Receptacle': 'Asset:Equipment:Electrical:ElectricalDistribution:ElectricalWiringDevice:ElectricalReceptacle',
    'SPECIAL REC.': 'Asset:Equipment:Electrical:ElectricalDistribution:ElectricalWiringDevice:ElectricalReceptacle',
    'SA_Duplex TP Receptacle': 'Asset:Equipment:Electrical:ElectricalDistribution:ElectricalWiringDevice:ElectricalReceptacle',
    'SA_DuplexIG Receptacle': 'Asset:Equipment:Electrical:ElectricalDistribution:ElectricalWiringDevice:ElectricalReceptacle',
    'SA_Ceiling Junction Box': 'Asset:Equipment:Electrical:ElectricalEquipment',
    'EF_NH_FLOOR-DUPLEX': 'Asset:Equipment:Electrical:ElectricalEquipment',
    'AMX - MVP-WDS': 'Asset:Equipment:Electrical:ElectricalEquipment',
    'SA_Junction Box': 'Asset:Equipment:Electrical:ElectricalEquipment',
    'SA_Quadruplex Receptacle (IG)': 'Asset:Equipment:Electrical:ElectricalDistribution:ElectricalWiringDevice:ElectricalReceptacle',
    'SA_Wall Junction Box': 'Asset:Equipment:Electrical:ElectricalEquipment',
    'Floor Quadruplex Receptacle': 'Asset:Equipment:Electrical:ElectricalDistribution:ElectricalWiringDevice:ElectricalReceptacle',
    'SA_Duplex Receptacle_3phase': 'Asset:Equipment:Electrical:ElectricalDistribution:ElectricalWiringDevice:ElectricalReceptacle',
    'SA_Duplex Rec': 'Asset:Equipment:Electrical:ElectricalDistribution:ElectricalWiringDevice:ElectricalReceptacle',
    'Motor': 'Asset:Equipment:Electrical:ElectricalEquipment',
    'Motor Switch': 'Asset:Equipment:Electrical:ElectricalEquipment',
    'SA_Floor Duplex Receptacle': 'Asset:Equipment:Electrical:ElectricalDistribution:ElectricalWiringDevice:ElectricalReceptacle',
    'SA_Quadruplex Receptacle': 'Asset:Equipment:Electrical:ElectricalDistribution:ElectricalWiringDevice:ElectricalReceptacle',
    'Switch': 'Asset:Equipment:Electrical:ElectricalEquipment',
    'SA_floor Junction Box': 'Asset:Equipment:Electrical:ElectricalEquipment',
    'SA_Wall Junction Box_3phase': 'Asset:Equipment:Electrical:ElectricalEquipment',
    'SA_Duplex Receptacle_208V': 'Asset:Equipment:Electrical:ElectricalDistribution:ElectricalWiringDevice:ElectricalReceptacle',
    'SPECIAL REC (3 phase)': 'Asset:Equipment:Electrical:ElectricalDistribution:ElectricalWiringDevice:ElectricalReceptacle',
    '480V Wall JBox': 'Asset:Equipment:Electrical:ElectricalEquipment',
    'SA_Special Receptacle L5-20R': 'Asset:Equipment:Electrical:ElectricalDistribution:ElectricalWiringDevice:ElectricalReceptacle',
    'SA_Wall 208-1P Junction Box': 'Asset:Equipment:Electrical:ElectricalEquipment',
    'SA_Pilot Light': 'Asset:Equipment:Electrical:ElectricalEquipment',
    'DD FUSED DISC-3p.SW2': 'Asset:Equipment:Electrical:ElectricalEquipment',
    'SA_Ceiling Receptacle': 'Asset:Equipment:Electrical:ElectricalDistribution:ElectricalWiringDevice:ElectricalReceptacle',
    'Telephone Outlet - Data': 'Asset:Equipment:Electrical:ElectricalDistribution:ElectricalWiringDevice:ElectricalReceptacle',
    'Telephone Outlet': 'Asset:Equipment:Electrical:ElectricalDistribution:ElectricalWiringDevice:ElectricalReceptacle',
    'SA_Switch Board': 'Asset:Equipment:Electrical:ElectricalDistribution:Switchboard',
    'Lighting and Appliance Panelboard - 208V MLO - Surface': 'Asset:Equipment:Electrical:ElectricalDistribution:ElectricalPanelboard:ElectricalPanelboardMLO',
    'Lighting and Appliance Panelboard - 480V MLO - Surface': 'Asset:Equipment:Electrical:ElectricalDistribution:ElectricalPanelboard:ElectricalPanelboardMLO',
    'Automatic Transfer Switch': 'Asset:Equipment:Electrical:ElectricalDistribution:TransferSwitch',
    'Disconnect Switches': 'Asset:Equipment:Electrical:ElectricalDistribution:DisconnectSwitch',
    'Dry Type Transformer - 480-208Y120 - NEMA Type 2': 'Asset:Equipment:Electrical:ElectricalDistribution:Transformer',
    'SA_Switch Board without EM': 'Asset:Equipment:Electrical:ElectricalDistribution:Switchboard',
    'Lighting and Appliance Panelboard - 480V MCB - Surface': 'Asset:Equipment:Electrical:ElectricalDistribution:ElectricalPanelboard:ElectricalPanelboardMCB',
    'Lighting and Appliance Panelboard - 208V MCB - Surface': 'Asset:Equipment:Electrical:ElectricalDistribution:ElectricalPanelboard:ElectricalPanelboardMCB',
    'Telephone Terminal Board': 'Asset:Equipment:Electrical:ElectricalDistribution:ElectricalPanelboard',
    'DISC.SW 208-480V': 'Asset:Equipment:Electrical:ElectricalDistribution:DisconnectSwitch',
    'ightning_Rod': 'Asset:Equipment:Electrical',
    'vfd': 'Asset:Equipment:Electrical:ElectricalDistribution:VariableFrequencyDrive',
    'Combination Starter - Disconnect Switches': 'Asset:Equipment:Electrical:ElectricalDistribution:DisconnectSwitch',
    'FUSED DISC-3p.SW2': 'Asset:Equipment:Electrical:ElectricalDistribution:DisconnectSwitch',
    'Inverter': 'Asset:Equipment:Electrical',
    'Gas Emergency Power Generator': 'Asset:Equipment:Electrical:ElectricalGenerationStorage:Generator',
    'ELectrical Meter': 'Asset:Equipment:Meter:ElectricalMeter',
    'Wire trough': 'Asset:Equipment:Electrical:ElectricalDistribution:ElectricalWiringDevice',
    'Dimmer Panel': 'Asset:Equipment:Electrical:ElectricalDistribution:ElectricalPanelboard',
    'Combination Starter - Disconnect Switches 480V': 'Asset:Equipment:Electrical:ElectricalDistribution:DisconnectSwitch',
    'SA_Pull Box': 'Asset:Equipment:Electrical',
    'Clock': 'BuildingComponent',
    'Bell': 'BuildingComponent',
    'Basic Wall': 'BuildingComponent:Architectural:Wall',
    # Havtech 
    'Lamp Post - Dbl': 'Asset:Equipment:Lighting',
    'Lighting-Recessed-Ledalite-PureFX-LED-2x': 'Asset:Equipment:Lighting',
    'WP': 'Asset:Equipment:Lighting',
    'AF-6-Open-TRT': 'Asset:Equipment:Lighting',
    'SS': 'Asset:Equipment:Lighting',
    'SP8 2x4': 'Asset:Equipment:Lighting',
    'Lighting-LED-LSI_Industries-XGBWM3': 'Asset:Equipment:Lighting',
    'FGB24': 'Asset:Equipment:Lighting',
    'SA_Wall Exit without arrow': 'Asset:Equipment:Lighting',
    'Soda Dispensing Machine': 'Asset:Equipment:Foodservice:Beverage',
    'Refrigerator': 'Asset:Equipment:Foodservice:FoodStorage:Refrigeration:RefrigerationEquipment',
    'Gas Range': 'Asset:Equipment:Electrical',
    'DipperWell': 'Asset:Equipment:Electrical',
    'Gas Griddle': 'Asset:Equipment:Electrical',
    'SA_Receptacle-Quad': 'Asset:Equipment:Electrical:ElectricalDistribution:ElectricalWiringDevice:ElectricalReceptacle',
    'SA_Floor Duplex Receptacle ': 'Asset:Equipment:Electrical:ElectricalDistribution:ElectricalWiringDevice:ElectricalReceptacle',
    'Telephone Outlet - Dual': 'Asset:Equipment:Electrical:ElectricalDistribution:ElectricalWiringDevice:ElectricalReceptacle',

    # Plumbing 
    'Bend - PVC - Sch 40 - DWV': 'Asset:DistributionAsset:DistributionConnector:PipeFitting',
    'Transition - Generic': 'Asset:DistributionAsset:DistributionConnector:PipeFitting',
    'P-TRAP': 'Asset:DistributionAsset:DistributionConnector:PipeFitting',
    'Elbow - Generic': 'Asset:DistributionAsset:DistributionConnector:PipeFitting',
    'Tee - Generic': 'Asset:DistributionAsset:DistributionConnector:PipeFitting',
    'Pipe Plain Wye - DWV - Glued': 'Asset:DistributionAsset:DistributionConnector:PipeFitting',
    'Wye 45 Deg - PVC - Sch 40 - DWV': 'Asset:DistributionAsset:DistributionConnector:PipeFitting',
    'Pipe Reducing Wye - DWV - Glued': 'Asset:DistributionAsset:DistributionConnector:PipeFitting',
    'Reducer - PVC - Sch 40 - DWV': 'Asset:DistributionAsset:DistributionConnector:PipeFitting',
    'Tee Sanitary - PVC - Sch 40 - DWV': 'Asset:DistributionAsset:DistributionConnector:PipeFitting',
    'Pipe Plug - PVC': 'Asset:DistributionAsset:DistributionConnector:PipeFitting',
    'Pipe-Fitting_Short-Quarter-Bend_PVC-DWV_300-A_Charlotte': 'Asset:DistributionAsset:DistributionConnector:PipeFitting',
    'Coupling - Generic': 'Asset:DistributionAsset:DistributionConnector:PipeFitting',
    'Wye Combination with 8th Bend Double - PVC - Sch 40 - DWV': 'Asset:DistributionAsset:DistributionConnector:PipeFitting',
    'Wye 45 Deg Reducing Double - PVC - Sch 40 - DWV': 'Asset:DistributionAsset:DistributionConnector:PipeFitting',
    'Pipe Types': 'Asset:DistributionAsset:Pipe',
    'Floor Drain - Round': 'Asset:Equipment:Plumbing:Drain:FloorDrain',
    'Round Floor Drain': 'Asset:Equipment:Plumbing:Drain:FloorDrain',
    'Lavatory - Wall Mounted': 'Asset:Equipment:Plumbing:PlumbingFixture:Sink',
    'Water Closet - Flush Valve - Wall Mounted': 'Asset:Equipment:Plumbing:PlumbingFixture:Toilet',
    'RainwaterTank': 'Asset:Equipment:Plumbing:PlumbingTank',
    'Floor Drain - Rectangular': 'Asset:Equipment:Plumbing:Drain:FloorDrain',
    'Urinal-WalMount_CoastGuard': 'Asset:Equipment:Plumbing:PlumbingFixture:Urinal',
    '1000gallonGreaseInterceptor': 'Asset:Equipment:Plumbing',
    'Sink - Lab-Single': 'Asset:Equipment:Plumbing:PlumbingFixture:Sink',
    'Roof_Drain_1010_JRSmith': 'Asset:Equipment:Plumbing:Drain:RoofDrain',
    'Sink - Island - Single': 'Asset:Equipment:Plumbing:PlumbingFixture:Sink',
    'Sink - Work': 'Asset:Equipment:Plumbing:PlumbingFixture:Sink',
    'Fountain-Eyewash-Bradley_Corp-S19-310K': 'Asset:Equipment:Plumbing:PlumbingFixture',
    'Sink - Service': 'Asset:Equipment:Plumbing:PlumbingFixture:Sink',
    '930': 'Asset:Equipment:Plumbing:PlumbingFixture',
    'Drinking Fountain - BiLevel': 'Asset:Equipment:Plumbing:PlumbingFixture:DrinkingFountain',
    'Interceptor_8000-8100_JRSmith': 'Asset:Equipment:Plumbing:PlumbingFixture',
    'Sanitary_Floor_Drain_3410_JRSmith': 'Asset:Equipment:Plumbing:Drain:FloorDrain',
    '6FootTrench': 'Asset:Equipment:Plumbing:PlumbingFixture',
    '4foot4Trench': 'Asset:Equipment:Plumbing:PlumbingFixture',
    '5footTrench': 'Asset:Equipment:Plumbing:PlumbingFixture',
    'Advance-Tabco_Floor_Trough_X_by_Y_parametric_8562': 'Asset:Equipment:Plumbing:PlumbingFixture',
    'Rectangular Elbow - Mitered': 'Asset:DistributionAsset:DistributionConnector:HVACDuctFitting',
    'Gate Valve - 2-12 Inch': 'Asset:Equipment:Plumbing:Valve:PlumbingValve',
    'Balancing Valve - Straight - 0.5-2 Inch - Threaded': 'Asset:Equipment:Plumbing:Valve:PlumbingBalancingValve',
    'Double Check Valve reg- 2.5-10 Inch': 'Asset:Equipment:Plumbing:Valve:PlumbingValve',
    'Pressure Regulating Valve - 2-6 Inch - Flanged': 'Asset:Equipment:Plumbing:Valve:PlumbingValve',
    'Solenoid Valve - 0.5-3 Inch': 'Asset:Equipment:Plumbing:Valve:PlumbingValve',
    'Y Strainer - 2-20 Inch - Flanged': 'Asset:Equipment:Plumbing',
    'Backflow Preventer - 0.5-2 Inch': 'Asset:Equipment:Plumbing',
    'Water_Meter_-_MVR350_5941': 'Asset:Equipment:Plumbing',
    'Pressure Regulating Valve - 0.5-2 Inch - Threaded': 'Asset:Equipment:Plumbing:Valve:PlumbingValve',
    '3 Way Valve - 0.75-4 Inch': 'Asset:Equipment:Plumbing:Valve:PlumbingValve',
    #Havtech
    'Elbow - Wrought Copper - ACR': 'Asset:DistributionAsset:DistributionConnector:PipeFitting',
    'Tee - Wrought Copper - ACR': 'Asset:DistributionAsset:DistributionConnector:PipeFitting',
    'Transition - Generic': 'Asset:DistributionAsset:DistributionConnector:PipeFitting',
    'Tee Reducing Sanitary - PVC - Sch 40 - DWV': 'Asset:DistributionAsset:DistributionConnector:PipeFitting',
    'Plug - PVC - Sch 40 - DWV': 'Asset:DistributionAsset:DistributionConnector:PipeFitting',
    'Tee - Welded - Generic': 'Asset:DistributionAsset:DistributionConnector:PipeFitting',
    'Buttweld Elbow (LR)': 'Asset:DistributionAsset:DistributionConnector:PipeFitting',
    'Buttweld Reducer': 'Asset:DistributionAsset:DistributionConnector:PipeFitting',
    'Cap - Welded - Generic': 'Asset:DistributionAsset:DistributionConnector:PipeFitting',
    '3461.001(1.6)': 'Asset:Equipment:Plumbing:PlumbingFixture:Toilet',
    'flushometer-top-spud-sloan-uppercut-wes-111': 'Asset:Equipment:Plumbing:PlumbingFixture:Toilet:ToiletFlushometer',
    '9140.047': 'Asset:Equipment:Plumbing:PlumbingFixture:Sink',
    '6590.001': 'Asset:Equipment:Plumbing:PlumbingFixture:Urinal',
    '0426-000_rfa': 'Asset:Equipment:Plumbing:PlumbingFixture:Sink',
    'equip-sink-elkay-single-quartz-ada-2522': 'Asset:Equipment:Plumbing:PlumbingFixture:Sink',
    'Flr_Drn_2005_Rnd-A_JRSmith': 'Asset:Equipment:Plumbing:PlumbingFixture',
    '3 Compartment Sink': 'Asset:Equipment:Plumbing:PlumbingFixture:Sink',
    'Gas Fryer': 'Asset:Equipment:Plumbing',
    'A.O. SMITH BTH-120': 'Asset:Equipment:Plumbing:WaterHeater:TankWaterHeater:GasTankWaterHeater',
    'Sink Vanity-Square': 'Asset:Equipment:Plumbing:PlumbingFixture:Sink',
    'Janitors Sink': 'Asset:Equipment:Plumbing:PlumbingFixture:Sink',
    '830-AA': 'Asset:Equipment:Plumbing:PlumbingFixture:Faucet',
    'TM-186-8015-PRV': 'Asset:DistributionAsset:DistributionConnector:PipeFitting'
}