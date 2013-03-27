init:
    
    #Main Character
    
    # 雨宮聡介 (あめみや そうすけ)
    define so = Character(u"聡介")
    
    # 首館 あやめ (くびたち あやめ)
    define ay = Character(u"あやめ", color="#d47e61")
    
    # 犬哭 キリコ (いぬなき きりこ)
    define ki = Character(u"キリコ", color="#ff6479")
    
    # 朽無 みそぎ (くちなし みそぎ)
    define mi = Character(u"みそぎ", color="#b6b3eb")
    
    # 雨宮 しとね (あめみや しとね)
    define si = Character(u"しとね", color="#ffaed4")
    
    #Sub Character
    
    # 進藤 明良 (しんどう あきら)
    define ak = Character(u"明良", color="#567e9c")
    
    # ベッキー / 先生
    define be = Character(u"ベッキー")
    
    # 城嶋 譲治 (じょうしま じょうじ) / 先生
    define jo = Character(u"城嶋")
    
    # 木戸 零佳 (きど れいか)
    define re = Character(u"零佳", color="#6e6e8d")
    
    #Variable
    $ loveAy = 0
    $ loveKi = 0
    $ loveMi = 0
    $ loveSi = 0
    
    #Background image
    image bg school classroom = "image/bg/bg_a00.jpg"
    image bg school passage = "image/bg/bg_a01.jpg"
    image bg school staircase = "image/bg/bg_a02.jpg"
    image bg school shoebox = "image/bg/bg_a03.jpg"
    image bg school gate = "image/bg/bg_a04.jpg"
    image bg school schoolyard = "image/bg/bg_a05.jpg"
    image bg bg_a06 = "image/bg/bg_a06.jpg"
    image bg bg_a07 = "image/bg/bg_a07.jpg"
    image bg bg_a08 = "image/bg/bg_a08.jpg"
    image bg bg_a09 = "image/bg/bg_a09.jpg"
    image bg bg_a10 = "image/bg/bg_a10.jpg"
    image bg bg_a11 = "image/bg/bg_a11.jpg"
    image bg bg_a12 = "image/bg/bg_a12.jpg"
    image bg bg_a13 = "image/bg/bg_a13.jpg"
    image bg bg_a14 = "image/bg/bg_a14.jpg"
    image bg bg_a15 = "image/bg/bg_a15.jpg"
    image bg bg_a16 = "image/bg/bg_a16.jpg"
    image bg bg_a17 = "image/bg/bg_a17.jpg"
    image bg bg_a18 = "image/bg/bg_a18.jpg"
    image bg bg_a19 = "image/bg/bg_a19.jpg"
    image bg bg_a20 = "image/bg/bg_a20.jpg"
    image bg bg_a21 = "image/bg/bg_a21.jpg"
    image bg bg_a22 = "image/bg/bg_a22.jpg"
    image bg bg_b00 = "image/bg/bg_b00.jpg"
    image bg bg_b01 = "image/bg/bg_b01.jpg"
    image bg bg_b02 = "image/bg/bg_b02.jpg"
    image bg bg_b02a = "image/bg/bg_b02a.jpg"
    image bg bg_b03 = "image/bg/bg_b03.jpg"
    image bg bg_b04 = "image/bg/bg_b04.jpg"
    image bg bg_b05 = "image/bg/bg_b05.jpg"
    image bg bg_b06 = "image/bg/bg_b06.jpg"
    image bg bg_b07 = "image/bg/bg_b07.jpg"
    image bg bg_c00 = "image/bg/bg_c00.jpg"
    image bg bg_c01 = "image/bg/bg_c01.jpg"
    image bg bg_c02 = "image/bg/bg_c02.jpg"
    image bg bg_c03 = "image/bg/bg_c03.jpg"
    image bg bg_c04 = "image/bg/bg_c04.jpg"
    image bg bg_c05 = "image/bg/bg_c05.jpg"
    image bg bg_c06 = "image/bg/bg_c06.jpg"
    image bg bg_c08 = "image/bg/bg_c08.jpg"
    image bg bg_c09 = "image/bg/bg_c09.jpg"
    image bg bg_c10 = "image/bg/bg_c10.jpg"
    image bg bg_c11 = "image/bg/bg_c11.jpg"
    image bg bg_c12 = "image/bg/bg_c12.jpg"
    image bg bg_c13 = "image/bg/bg_c13.jpg"
    image bg bg_d00 = "image/bg/bg_d00.jpg"
    image bg bg_d01 = "image/bg/bg_d01.jpg"
    image bg bg_d02 = "image/bg/bg_d02.jpg"
    image bg bg_d03 = "image/bg/bg_d03.jpg"
    image bg bg_d04 = "image/bg/bg_d04.jpg"
    image bg bg_d05 = "image/bg/bg_d05.jpg"
    image bg bg_d06 = "image/bg/bg_d06.jpg"
    image bg bg_d07 = "image/bg/bg_d07.jpg"
    image bg bg_d08 = "image/bg/bg_d08.jpg"
    image bg bg_d09 = "image/bg/bg_d09.jpg"
    image bg bg_d10 = "image/bg/bg_d10.jpg"
    image bg bg_e00 = "image/bg/bg_e00.jpg"
    image bg bg_e01 = "image/bg/bg_e01.jpg"
    image bg bg_e02 = "image/bg/bg_e02.jpg"
    image bg bg_e03 = "image/bg/bg_e03.jpg"
    image bg bg_e04 = "image/bg/bg_e04.jpg"
    image bg bg_e05 = "image/bg/bg_e05.jpg"
    image bg bg_e06 = "image/bg/bg_e06.jpg"
    image bg bg_e07 = "image/bg/bg_e07.jpg"
    image bg bg_e08 = "image/bg/bg_e08.jpg"
    image bg bg_e09 = "image/bg/bg_e09.jpg"
    image bg bg_f00 = "image/bg/bg_f00.jpg"
    image bg bg_f01 = "image/bg/bg_f01.jpg"
    image bg bg_f02 = "image/bg/bg_f02.jpg"
    image bg bg_f03 = "image/bg/bg_f03.jpg"
    image bg bg_g00 = "image/bg/bg_g00.jpg"
    image bg bg_g01 = "image/bg/bg_g01.jpg"
    image bg bg_g02 = "image/bg/bg_g02.jpg"
    image bg bg_g03 = "image/bg/bg_g03.jpg"
    image bg bg_g04 = "image/bg/bg_g04.jpg"
    image bg bg_h00 = "image/bg/bg_h00.jpg"
    image bg bg_h01 = "image/bg/bg_h01.jpg"
    image bg bg_h02 = "image/bg/bg_h02.jpg"
    image bg bg_h03 = "image/bg/bg_h03.jpg"
    image bg bg_h04 = "image/bg/bg_h04.jpg"
    image bg bg_h05 = "image/bg/bg_h05.jpg"
    image bg bg_h06 = "image/bg/bg_h06.jpg"
    image bg bg_h07 = "image/bg/bg_h07.jpg"
    image bg bg_h08 = "image/bg/bg_h08.jpg"
    image bg bg_i00 = "image/bg/bg_i00.jpg"
    image bg bg_i01 = "image/bg/bg_i01.jpg"
    image bg bg_i02 = "image/bg/bg_i02.jpg"
    image bg bg_i03 = "image/bg/bg_i03.jpg"
    image bg bg_i04 = "image/bg/bg_i04.jpg"
    image bg bg_j00 = "image/bg/bg_j00.jpg"
    image bg bg_j01 = "image/bg/bg_j01.jpg"
    image bg bg_s00 = "image/bg/bg_s00.jpg"
    image bg bg_s01 = "image/bg/bg_s01.jpg"
    image bg bg_s02 = "image/bg/bg_s02.jpg"
    image bg bg_s04 = "image/bg/bg_s04.jpg"
    image bg bg_z00 = "image/bg/bg_z00.jpg"
    
    #CG
    image cg cg_aa_01 = "image/cg/cg_aa_01.png"
    image cg cg_aa_02 = "image/cg/cg_aa_02.jpg"
    image cg cg_aya_01 = "image/cg/cg_aya_01.png"
    image cg cg_aya_02 = "image/cg/cg_aya_02.png"
    image cg cg_ki_01 = "image/cg/cg_ki_01.png"
    image cg cg_ki_02 = "image/cg/cg_ki_02.png"
    image cg cg_ki_03 = "image/cg/cg_ki_03.png"
    image cg cg_ki_04 = "image/cg/cg_ki_04.png"
    image cg cg_ki_05 = "image/cg/cg_ki_05.png"
    image cg cg_mi_01 = "image/cg/cg_mi_01.png"
    image cg cg_mi_02 = "image/cg/cg_mi_02.png"
    image cg cg_mi_03 = "image/cg/cg_mi_03.png"
    image cg cg_mi_04 = "image/cg/cg_mi_04.png"
    image cg cg_mi_05 = "image/cg/cg_mi_05.png"
    image cg cg_mi_07 = "image/cg/cg_mi_07.png"
    image cg cg_mi_08 = "image/cg/cg_mi_08.png"
    image cg cg_mi_09 = "image/cg/cg_mi_09.png"
    image cg cg_mi_10 = "image/cg/cg_mi_10.png"
    image cg cg_si_01 = "image/cg/cg_si_01.png"
    image cg cg_si_02 = "image/cg/cg_si_02.png"
    image cg cg_si_03 = "image/cg/cg_si_03.png"
    image cg title = "image/cg/title.jpg"
    
    #Character image
    
    # 進藤 明良 (しんどう あきら)
    image akira aki_1_01 = "image/fg/akira/aki_1_01.png"
    image akira aki_1_02 = "image/fg/akira/aki_1_02.png"
    image akira aki_1_03 = "image/fg/akira/aki_1_03.png"
    image akira aki_1_04 = "image/fg/akira/aki_1_04.png"
    image akira aki_1_05 = "image/fg/akira/aki_1_05.png"
    image akira aki_1_06 = "image/fg/akira/aki_1_06.png"
    image akira aki_1_07 = "image/fg/akira/aki_1_07.png"
    image akira aki_1_08 = "image/fg/akira/aki_1_08.png"
    image akira aki_1_09 = "image/fg/akira/aki_1_09.png"
    image akira aki_1_10 = "image/fg/akira/aki_1_10.png"
    image akira aki_1_11 = "image/fg/akira/aki_1_11.png"
    image akira aki_1_12 = "image/fg/akira/aki_1_12.png"
    image akira aki_1_13 = "image/fg/akira/aki_1_13.png"
    
    # 首館 あやめ (くびたち あやめ)
    image ayame aya_1_01 = "image/fg/ayame/aya_1_01.png"
    image ayame aya_1_02 = "image/fg/ayame/aya_1_02.png"
    image ayame aya_1_03 = "image/fg/ayame/aya_1_03.png"
    image ayame aya_1_04 = "image/fg/ayame/aya_1_04.png"
    image ayame aya_1_05 = "image/fg/ayame/aya_1_05.png"
    image ayame aya_1_07 = "image/fg/ayame/aya_1_07.png"
    image ayame aya_1_08 = "image/fg/ayame/aya_1_08.png"
    image ayame aya_1_09 = "image/fg/ayame/aya_1_09.png"
    image ayame aya_1_10 = "image/fg/ayame/aya_1_10.png"
    image ayame aya_1_21 = "image/fg/ayame/aya_1_21.png"
    image ayame aya_2_01 = "image/fg/ayame/aya_2_01.png"
    image ayame aya_2_02 = "image/fg/ayame/aya_2_02.png"
    image ayame aya_2_07 = "image/fg/ayame/aya_2_07.png"
    image ayame aya_2_08 = "image/fg/ayame/aya_2_08.png"
    image ayame aya_3_01 = "image/fg/ayame/aya_3_01.png"
    image ayame aya_3_02 = "image/fg/ayame/aya_3_02.png"
    image ayame aya_3_03 = "image/fg/ayame/aya_3_03.png"
    image ayame aya_3_07 = "image/fg/ayame/aya_3_07.png"
    image ayame aya_3_08 = "image/fg/ayame/aya_3_08.png"
    image ayame aya_4_01 = "image/fg/ayame/aya_4_01.png"
    image ayame aya_4_02 = "image/fg/ayame/aya_4_02.png"
    image ayame aya_4_05 = "image/fg/ayame/aya_4_05.png"
    image ayame aya_4_07 = "image/fg/ayame/aya_4_07.png"
    image ayame aya_4_08 = "image/fg/ayame/aya_4_08.png"
    
    # 犬哭 キリコ (いぬなき きりこ)
    image kiriko ki_1_01 = "image/fg/kiriko/ki_1_01.png"
    image kiriko ki_1_02 = "image/fg/kiriko/ki_1_02.png"
    image kiriko ki_1_02a = "image/fg/kiriko/ki_1_02a.png"
    image kiriko ki_1_03 = "image/fg/kiriko/ki_1_03.png"
    image kiriko ki_1_04 = "image/fg/kiriko/ki_1_04.png"
    image kiriko ki_1_05 = "image/fg/kiriko/ki_1_05.png"
    image kiriko ki_1_06 = "image/fg/kiriko/ki_1_06.png"
    image kiriko ki_1_07 = "image/fg/kiriko/ki_1_07.png"
    image kiriko ki_1_08 = "image/fg/kiriko/ki_1_08.png"
    image kiriko ki_2_01 = "image/fg/kiriko/ki_2_01.png"
    image kiriko ki_2_02 = "image/fg/kiriko/ki_2_02.png"
    image kiriko ki_2_02a = "image/fg/kiriko/ki_2_02a.png"
    image kiriko ki_2_03 = "image/fg/kiriko/ki_2_03.png"
    image kiriko ki_2_04 = "image/fg/kiriko/ki_2_04.png"
    image kiriko ki_2_05 = "image/fg/kiriko/ki_2_05.png"
    image kiriko ki_2_06 = "image/fg/kiriko/ki_2_06.png"
    image kiriko ki_2_07 = "image/fg/kiriko/ki_2_07.png"
    image kiriko ki_2_08 = "image/fg/kiriko/ki_2_08.png"
    image kiriko ki_2_09 = "image/fg/kiriko/ki_2_09.png"
    image kiriko ki_3_01 = "image/fg/kiriko/ki_3_01.png"
    image kiriko ki_3_02 = "image/fg/kiriko/ki_3_02.png"
    image kiriko ki_3_06 = "image/fg/kiriko/ki_3_06.png"
    image kiriko ki_4_01 = "image/fg/kiriko/ki_4_01.png"
    image kiriko ki_4_02 = "image/fg/kiriko/ki_4_02.png"
    image kiriko ki_4_06 = "image/fg/kiriko/ki_4_06.png"
    image kiriko ki_5_01 = "image/fg/kiriko/ki_5_01.png"
    image kiriko ki_5_02 = "image/fg/kiriko/ki_5_02.png"
    image kiriko ki_5_03 = "image/fg/kiriko/ki_5_03.png"
    image kiriko ki_5_04 = "image/fg/kiriko/ki_5_04.png"
    image kiriko ki_5_05 = "image/fg/kiriko/ki_5_05.png"
    image kiriko ki_5_07 = "image/fg/kiriko/ki_5_07.png"
    image kiriko ki_5_08 = "image/fg/kiriko/ki_5_08.png"
    image kiriko ki_6_01 = "image/fg/kiriko/ki_6_01.png"
    image kiriko ki_6_02 = "image/fg/kiriko/ki_6_02.png"
    image kiriko ki_6_03 = "image/fg/kiriko/ki_6_03.png"
    image kiriko ki_6_04 = "image/fg/kiriko/ki_6_04.png"
    image kiriko ki_6_05 = "image/fg/kiriko/ki_6_05.png"
    image kiriko ki_6_07 = "image/fg/kiriko/ki_6_07.png"
    image kiriko ki_6_08 = "image/fg/kiriko/ki_6_08.png"
    
    # 朽無 みそぎ (くちなし みそぎ)
    image misogi mi_1_01 = "image/fg/misogi/mi_1_01.png"
    image misogi mi_1_02 = "image/fg/misogi/mi_1_02.png"
    image misogi mi_1_02a = "image/fg/misogi/mi_1_02a.png"
    image misogi mi_1_03 = "image/fg/misogi/mi_1_03.png"
    image misogi mi_1_04 = "image/fg/misogi/mi_1_04.png"
    image misogi mi_1_05 = "image/fg/misogi/mi_1_05.png"
    image misogi mi_1_05a = "image/fg/misogi/mi_1_05a.png"
    image misogi mi_1_06a = "image/fg/misogi/mi_1_06a.png"
    image misogi mi_1_06b = "image/fg/misogi/mi_1_06b.png"
    image misogi mi_1_06c = "image/fg/misogi/mi_1_06c.png"
    image misogi mi_1_07 = "image/fg/misogi/mi_1_07.png"
    image misogi mi_1_08 = "image/fg/misogi/mi_1_08.png"
    image misogi mi_1_09 = "image/fg/misogi/mi_1_09.png"
    image misogi mi_1_10 = "image/fg/misogi/mi_1_10.png"
    image misogi mi_1_11 = "image/fg/misogi/mi_1_11.png"
    image misogi mi_1_20 = "image/fg/misogi/mi_1_20.png"
    image misogi mi_1_21 = "image/fg/misogi/mi_1_21.png"
    image misogi mi_2_01 = "image/fg/misogi/mi_2_01.png"
    image misogi mi_2_02 = "image/fg/misogi/mi_2_02.png"
    image misogi mi_2_03 = "image/fg/misogi/mi_2_03.png"
    image misogi mi_2_05 = "image/fg/misogi/mi_2_05.png"
    image misogi mi_2_05a = "image/fg/misogi/mi_2_05a.png"
    image misogi mi_2_06a = "image/fg/misogi/mi_2_06a.png"
    image misogi mi_2_06b = "image/fg/misogi/mi_2_06b.png"
    image misogi mi_2_06c = "image/fg/misogi/mi_2_06c.png"
    image misogi mi_2_07 = "image/fg/misogi/mi_2_07.png"
    image misogi mi_2_08 = "image/fg/misogi/mi_2_08.png"
    image misogi mi_2_09 = "image/fg/misogi/mi_2_09.png"
    image misogi mi_2_10 = "image/fg/misogi/mi_2_10.png"
    image misogi mi_2_11 = "image/fg/misogi/mi_2_11.png"
    image misogi mi_2_20 = "image/fg/misogi/mi_2_20.png"
    image misogi mi_3_01 = "image/fg/misogi/mi_3_01.png"
    image misogi mi_3_02 = "image/fg/misogi/mi_3_02.png"
    image misogi mi_3_02a = "image/fg/misogi/mi_3_02a.png"
    image misogi mi_3_03 = "image/fg/misogi/mi_3_03.png"
    image misogi mi_3_05 = "image/fg/misogi/mi_3_05.png"
    image misogi mi_3_05a = "image/fg/misogi/mi_3_05a.png"
    image misogi mi_3_06a = "image/fg/misogi/mi_3_06a.png"
    image misogi mi_3_06b = "image/fg/misogi/mi_3_06b.png"
    image misogi mi_3_06c = "image/fg/misogi/mi_3_06c.png"
    image misogi mi_3_07 = "image/fg/misogi/mi_3_07.png"
    image misogi mi_3_08 = "image/fg/misogi/mi_3_08.png"
    image misogi mi_4_01 = "image/fg/misogi/mi_4_01.png"
    image misogi mi_4_02 = "image/fg/misogi/mi_4_02.png"
    image misogi mi_4_06a = "image/fg/misogi/mi_4_06a.png"
    image misogi mi_4_06b = "image/fg/misogi/mi_4_06b.png"
    image misogi mi_4_06c = "image/fg/misogi/mi_4_06c.png"
    image misogi mi_4_07 = "image/fg/misogi/mi_4_07.png"
    image misogi mi_4_08 = "image/fg/misogi/mi_4_08.png"
    
    # 木戸 零佳 (きど れいか)
    image reika re_1_01 = "image/fg/reika/re_1_01.png"
    image reika re_1_02 = "image/fg/reika/re_1_02.png"
    image reika re_1_04 = "image/fg/reika/re_1_04.png"
    image reika re_1_05 = "image/fg/reika/re_1_05.png"
    image reika re_1_07 = "image/fg/reika/re_1_07.png"
    image reika re_1_21 = "image/fg/reika/re_1_21.png"
    image reika re_1_22 = "image/fg/reika/re_1_22.png"
    image reika re_1_24 = "image/fg/reika/re_1_24.png"
    image reika re_1_25 = "image/fg/reika/re_1_25.png"
    image reika re_2_01 = "image/fg/reika/re_2_01.png"
    image reika re_2_02 = "image/fg/reika/re_2_02.png"
    image reika re_2_04 = "image/fg/reika/re_2_04.png"
    image reika re_2_05 = "image/fg/reika/re_2_05.png"
    image reika re_2_21 = "image/fg/reika/re_2_21.png"
    image reika re_2_22 = "image/fg/reika/re_2_22.png"
    image reika re_2_24 = "image/fg/reika/re_2_24.png"
    image reika re_2_25 = "image/fg/reika/re_2_25.png"
    
    # 雨宮 しとね (あめみや しとね)
    image sitone si_1_01 = "image/fg/sitone/si_1_01.png"
    image sitone si_1_02 = "image/fg/sitone/si_1_02.png"
    image sitone si_1_02a = "image/fg/sitone/si_1_02a.png"
    image sitone si_1_03 = "image/fg/sitone/si_1_03.png"
    image sitone si_1_05 = "image/fg/sitone/si_1_05.png"
    image sitone si_1_06 = "image/fg/sitone/si_1_06.png"
    image sitone si_1_07 = "image/fg/sitone/si_1_07.png"
    image sitone si_1_08 = "image/fg/sitone/si_1_08.png"
    image sitone si_1_09 = "image/fg/sitone/si_1_09.png"
    image sitone si_1_10 = "image/fg/sitone/si_1_10.png"
    image sitone si_1_11 = "image/fg/sitone/si_1_11.png"
    image sitone si_1_12 = "image/fg/sitone/si_1_12.png"
    image sitone si_1_13 = "image/fg/sitone/si_1_13.png"
    image sitone si_1_14 = "image/fg/sitone/si_1_14.png"
    image sitone si_1_15 = "image/fg/sitone/si_1_15.png"
    image sitone si_1_20 = "image/fg/sitone/si_1_20.png"
    image sitone si_1_22 = "image/fg/sitone/si_1_22.png"
    image sitone si_1_23 = "image/fg/sitone/si_1_23.png"
    image sitone si_2_01 = "image/fg/sitone/si_2_01.png"
    image sitone si_2_02 = "image/fg/sitone/si_2_02.png"
    image sitone si_2_02a = "image/fg/sitone/si_2_02a.png"
    image sitone si_2_03 = "image/fg/sitone/si_2_03.png"
    image sitone si_2_04 = "image/fg/sitone/si_2_04.png"
    image sitone si_2_05 = "image/fg/sitone/si_2_05.png"
    image sitone si_2_06 = "image/fg/sitone/si_2_06.png"
    image sitone si_2_07 = "image/fg/sitone/si_2_07.png"
    image sitone si_2_08 = "image/fg/sitone/si_2_08.png"
    image sitone si_2_09 = "image/fg/sitone/si_2_09.png"
    image sitone si_2_10 = "image/fg/sitone/si_2_10.png"
    image sitone si_2_11 = "image/fg/sitone/si_2_11.png"
    image sitone si_2_20 = "image/fg/sitone/si_2_20.png"
    image sitone si_2_21 = "image/fg/sitone/si_2_21.png"
    image sitone si_2_22 = "image/fg/sitone/si_2_22.png"
    image sitone si_3_01 = "image/fg/sitone/si_3_01.png"
    image sitone si_3_02 = "image/fg/sitone/si_3_02.png"
    image sitone si_3_03 = "image/fg/sitone/si_3_03.png"
    image sitone si_4_01 = "image/fg/sitone/si_4_01.png"
    image sitone si_4_02 = "image/fg/sitone/si_4_02.png"
    image sitone si_4_03 = "image/fg/sitone/si_4_03.png"
    image sitone si_4_04 = "image/fg/sitone/si_4_04.png"
    image sitone si_4_05 = "image/fg/sitone/si_4_05.png"
    image sitone si_4_06 = "image/fg/sitone/si_4_06.png"
    image sitone si_4_07 = "image/fg/sitone/si_4_07.png"
    image sitone si_4_08 = "image/fg/sitone/si_4_08.png"
    image sitone si_4_09 = "image/fg/sitone/si_4_09.png"
    image sitone si_4_10 = "image/fg/sitone/si_4_10.png"
    image sitone si_4_11 = "image/fg/sitone/si_4_11.png"
    image sitone si_4_12 = "image/fg/sitone/si_4_12.png"
    image sitone si_4_13 = "image/fg/sitone/si_4_13.png"
    image sitone si_4_14 = "image/fg/sitone/si_4_14.png"
    image sitone si_4_15 = "image/fg/sitone/si_4_15.png"