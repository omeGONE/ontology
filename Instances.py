from Classes import *

city = Discipline("Город", "Передвижение по Городу")
xc = Discipline("Кросс-кантри", "Кросс-кантри")
dh = Discipline("СкорстнойСпуск", "Только спуск")
enduro = Discipline("Эндуро", "Подъемы и спуски по сложному рельефу")

santa_cruz_v10 = Bike("SantaCruzV10", dh)
specialized_epic = Bike("SpecializedEpic", xc)
trek_marlin = Bike("TrekMarlin", city)
trek_slash = Bike("TrekSlash", enduro)

fox36_factory160 = Fork("Fox36Factory160", trek_slash)
fox40_factory203 = Fork("Fox40Factory203", santa_cruz_v10)
rock_shox_sid100 = Fork("RockShoxSID100", specialized_epic)
suntour_XCT100 = Fork("SuntourXCT100", trek_marlin)

shimano_altus_8sp = Drivetrain("ShimanoAltus8sp", trek_marlin)
shimano_xt_12sp = Drivetrain("ShimanoXT12sp", specialized_epic)
sram_gx_dh_7sp = Drivetrain("SRAMGxDH7sp", santa_cruz_v10)
sram_x01_axs = Drivetrain("SRAMX01AXS", trek_slash)

shimano_hg200_marlin = Cassette("ShimanoHG200Marlin",
                                shimano_altus_8sp)
shimano_xt_cassette_epic = Cassette("ShimanoXTCassetteEpic",
                                shimano_xt_12sp)
sram_pg_720_v10 = Cassette("SRAMPG720V10", sram_gx_dh_7sp)
sram_xg_1295_slash = Cassette("SRAMXG1295Slash",
                                sram_x01_axs)

sram_11t_v10 = Sprocket("SRAM11TV10", sram_pg_720_v10)
sram_14t_v10 = Sprocket("SRAM14TV10", sram_pg_720_v10)
sram_28t_v10 = Sprocket("SRAM28TV10", sram_pg_720_v10)
shimano_10t_epic = Sprocket("Shimano10TEpic", shimano_xt_cassette_epic)
shimano_51t_epic = Sprocket("Shimano51TEpic", shimano_xt_cassette_epic)
shimano_11t_marlin = Sprocket("Shimano11TMarlin", shimano_hg200_marlin)
shimano_34t_marlin = Sprocket("Shimano34TMarlin", shimano_hg200_marlin)
sram_10t_slash = Sprocket("SRAM10TSlash", sram_xg_1295_slash)
sram_52t_slash = Sprocket("SRAM52TSlash", sram_xg_1295_slash)

sram_pg_720_v10.hasSprocket = sram_11t_v10, sram_14t_v10, sram_28t_v10
shimano_xt_cassette_epic.hasSprocket = shimano_10t_epic, shimano_51t_epic
shimano_hg200_marlin.hasSprocket = shimano_11t_marlin, shimano_34t_marlin
sram_xg_1295_slash.hasSprocket = sram_10t_slash, sram_52t_slash

shimano_saint_m820 = BrakeSystem("ShimanoSaintM820", santa_cruz_v10)
shimano_xt_m8100 = BrakeSystem("ShimanoXTM8100", specialized_epic)
tektro_hd_m275 = BrakeSystem("TektroHDM275", trek_marlin)
sram_code_rsc = BrakeSystem("SRAMCodeRSC", trek_slash)

shimano_rtm805_203_v10 = BrakeRotor("ShimanoRTM805203V10", shimano_saint_m820)
shimano_saint_caliper_v10 = BrakeCaliper("ShimanoSaintCaliperV10", shimano_saint_m820)
shimano_saint_lever_v10 = BrakeLever("ShimanoSaintLeverV10", shimano_saint_m820)
sram_x7_shifter_v10 = Shifter("SRAMX7ShifterV10", sram_gx_dh_7sp)
sram_gx_rd_v10 = Derailleur("SRAMGXRDV10", sram_gx_dh_7sp)

shimano_rtm800_180_epic = BrakeRotor("ShimanoRTM800180Epic", shimano_xt_m8100)
shimano_xt_caliper_epic = BrakeCaliper("ShimanoXTCaliperEpic", shimano_xt_m8100)
shimano_xt_lever_epic = BrakeLever("ShimanoXTLeverEpic", shimano_xt_m8100)
shimano_xt_shifter_epic = Shifter("ShimanoXTShifterEpic", shimano_xt_12sp)
shimano_xt_rd_epic = Derailleur("ShimanoXTRDEpic", shimano_xt_12sp)

tektro_rotor_160_marlin = BrakeRotor("TektroRotor160Marlin", tektro_hd_m275)
tektro_caliper_marlin = BrakeCaliper("TektroCaliperMarlin", tektro_hd_m275)
tektro_lever_marlin = BrakeLever("TektroLeverMarlin", tektro_hd_m275)
shimano_altus_shifter_marlin = Shifter("ShimanoAltusShifterMarlin", shimano_altus_8sp)
shimano_altus_rd_marlin = Derailleur("ShimanoAltusRDMarlin", shimano_altus_8sp)

sram_hs2_200_slash = BrakeRotor("SRAMHS2200Slash", sram_code_rsc)
sram_code_caliper_slash = BrakeCaliper("SRAMCodeCaliperSlash", sram_code_rsc)
sram_code_lever_slash = BrakeLever("SRAMCodeLeverSlash", sram_code_rsc)
sram_x01_pod_slash = Shifter("SRAMX01PODSlash", sram_x01_axs)
sram_x01_rd_slash = Derailleur("SRAMX01RDSlash", sram_x01_axs)