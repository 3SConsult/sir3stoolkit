Object Types, Properties, and Result Value Types
-----------------------------------------------

.. note:: Network Type: Water
   The below sections lists all table names from self.ObjectTypes_TableNames, along with their properties, result properties, and respective object type from self.ObjectTypes (needed for toolkit operations like self.InsertElement(), self.GetPropertiesOfElementType()). The value types of the properties are also listed.
   Every property both model data and result will be returned as a python str. For result properties, this report intentionally lists names only.

AGSN
^^^^
Object Type: ``AGSN_HydraulicProfile``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Lfdnr``
     - ``int32``
   * - ``Aktiv``
     - ``int32``
   * - ``AllNodesAndLinks``
     - ``dictionary`2``
   * - ``ObjsString``
     - ``string``
   * - ``MainWay``
     - ``iagsnway``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

No result properties found.

WIND
^^^^
Object Type: ``AirVessel``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Indatab``
     - ``int32``
   * - ``A``
     - ``single``
   * - ``Hb``
     - ``single``
   * - ``Vg0``
     - ``single``
   * - ``Pg0``
     - ``single``
   * - ``Tgas``
     - ``single``
   * - ``Fkatab``
     - ``string``
   * - ``Dn``
     - ``single``
   * - ``Zetapos``
     - ``single``
   * - ``Zetaneg``
     - ``single``
   * - ``Rgas``
     - ``single``
   * - ``Rpoly``
     - ``single``
   * - ``Ibla``
     - ``int32``
   * - ``Knotk``
     - ``string``
   * - ``Zkor``
     - ``single``
   * - ``Fkfstf``
     - ``string``
   * - ``Fkcont``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``Iplanung``
     - ``int32``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``SymbolGraf``
     - ``symbol1c_graf``
   * - ``SymbolFactor``
     - ``double``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``Angle``
     - ``double``
   * - ``bz.Fk``
     - ``string``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``HLUFT``
   * - ``IAKTIV``
   * - ``M``
   * - ``MAINELEMENT``
   * - ``PLUFT``
   * - ``QM``
   * - ``RHO``
   * - ``T``
   * - ``V``
   * - ``VOL``
   * - ``VOLDA``
   * - ``VOLGAS``
   * - ``WALTER``
   * - ``WST``

ARRW
^^^^
Object Type: ``Arrow``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Fkcont``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``SymbolFactor``
     - ``double``
   * - ``Angle``
     - ``double``
   * - ``bz.Fk``
     - ``string``

Result Properties
"""""""""""""""""

No result properties found.

ATMO
^^^^
Object Type: ``Atmosphere``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Patmos``
     - ``single``
   * - ``Indbarf``
     - ``int32``
   * - ``Tatmos``
     - ``single``
   * - ``Rgas``
     - ``single``
   * - ``Rpoly``
     - ``single``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

No result properties found.

VKNO
^^^^
Object Type: ``BlockConnectionNode``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Fkknot``
     - ``string``
   * - ``Fkcont``
     - ``string``
   * - ``Showname``
     - ``int32``
   * - ``Posname``
     - ``int32``
   * - ``Pointinsertx``
     - ``double``
   * - ``Pointinserty``
     - ``double``
   * - ``Symbolfact``
     - ``single``
   * - ``Displaymode``
     - ``int32``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

No result properties found.

PARI
^^^^
Object Type: ``CalcPari``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Nglopt``
     - ``int32``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.Epsp``
     - ``single``
   * - ``bz.Epsqm``
     - ``single``
   * - ``bz.Epst``
     - ``single``
   * - ``bz.Epspreg``
     - ``single``
   * - ``bz.Epsqmreg``
     - ``single``
   * - ``bz.Epstrsp``
     - ``single``
   * - ``bz.Ntrspiter``
     - ``int32``
   * - ``bz.Nziter``
     - ``int32``
   * - ``bz.Ntiter``
     - ``int32``

Result Properties
"""""""""""""""""

No result properties found.

ZEP2
^^^^
Object Type: ``CharacteristicLossTable``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Typ``
     - ``int32``
   * - ``Kvbzg``
     - ``single``
   * - ``Beschreibung``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Zeitoption``
     - ``int32``

Result Properties
"""""""""""""""""

No result properties found.

ZEP2_ROWS
^^^^^^^^^
Object Type: ``CharacteristicLossTable_Row``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Fk``
     - ``string``
   * - ``Phi``
     - ``single``
   * - ``Zetapos``
     - ``single``
   * - ``Zetaneg``
     - ``single``
   * - ``Kvrelpos``
     - ``single``
   * - ``Kvrelneg``
     - ``single``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

No result properties found.

CIRC
^^^^
Object Type: ``Circle``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Fkcont``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``LineWidthMM``
     - ``double``
   * - ``LineColor``
     - ``color``
   * - ``FillColor``
     - ``color``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``bz.Fk``
     - ``string``

Result Properties
"""""""""""""""""

No result properties found.

KOMP
^^^^
Object Type: ``Compressor``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``Unknown``
   * - ``Beschreibung``
     - ``Unknown``
   * - ``Fkkomk``
     - ``Unknown``
   * - ``Inda``
     - ``Unknown``
   * - ``Etam``
     - ``Unknown``
   * - ``Tfahraus``
     - ``Unknown``
   * - ``Tfahrein``
     - ``Unknown``
   * - ``Dndt``
     - ``Unknown``
   * - ``Dqndt``
     - ``Unknown``
   * - ``Dpdt``
     - ``Unknown``
   * - ``Ipverh``
     - ``Unknown``
   * - ``Pverhqn``
     - ``Unknown``
   * - ``Pverhdp``
     - ``Unknown``
   * - ``Etat``
     - ``Unknown``
   * - ``Ibrenng``
     - ``Unknown``
   * - ``Iprst``
     - ``Unknown``
   * - ``Fkantp``
     - ``Unknown``
   * - ``Fkcont``
     - ``Unknown``
   * - ``Idreferenz``
     - ``Unknown``
   * - ``Iplanung``
     - ``Unknown``
   * - ``Tk``
     - ``Unknown``
   * - ``Pk``
     - ``Unknown``
   * - ``InVariant``
     - ``Unknown``
   * - ``Xkor``
     - ``Unknown``
   * - ``Ykor``
     - ``Unknown``
   * - ``ShowDescription``
     - ``Unknown``
   * - ``PositionOfDescription``
     - ``Unknown``
   * - ``Angle``
     - ``Unknown``
   * - ``SymbolFactor``
     - ``Unknown``
   * - ``GeometriesDiffer``
     - ``Unknown``
   * - ``bz.Fk``
     - ``Unknown``
   * - ``bz.Inds``
     - ``Unknown``
   * - ``bz.Sw``
     - ``Unknown``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``DP``
   * - ``DT``
   * - ``EINAUS``
   * - ``ETAP``
   * - ``IAKTIV``
   * - ``IND``
   * - ``INDANT``
   * - ``M``
   * - ``MAINELEMENT``
   * - ``N``
   * - ``P``
   * - ``PE``
   * - ``PI``
   * - ``PK``
   * - ``PMAX``
   * - ``PRATIO``
   * - ``QN``
   * - ``QNBG``
   * - ``QNGES``
   * - ``TI``
   * - ``TK``
   * - ``YP``

KOMK
^^^^
Object Type: ``CompressorTable``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Typ``
     - ``int32``
   * - ``Fkfstf``
     - ``string``
   * - ``Tansaug``
     - ``single``
   * - ``Pansaug``
     - ``single``
   * - ``Nmax``
     - ``single``
   * - ``Nmin``
     - ``single``
   * - ``Etaps``
     - ``single``
   * - ``Beschreibung``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Zeitoption``
     - ``int32``

Result Properties
"""""""""""""""""

No result properties found.

KOMK_ROWS
^^^^^^^^^
Object Type: ``CompressorTable_Row``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Fk``
     - ``string``
   * - ``N``
     - ``single``
   * - ``Q``
     - ``single``
   * - ``Yp``
     - ``single``
   * - ``P``
     - ``single``
   * - ``Etap``
     - ``single``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

No result properties found.

CRGL
^^^^
Object Type: ``ControlEngineeringNexus``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Fkcont``
     - ``string``
   * - ``Idxke``
     - ``int32``
   * - ``LineWidthMM``
     - ``double``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

No result properties found.

RART
^^^^
Object Type: ``ControlMode``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Fkkref1``
     - ``string``
   * - ``Fkkref2``
     - ``string``
   * - ``Indstd``
     - ``int32``
   * - ``Xdein``
     - ``single``
   * - ``Tsig``
     - ``single``
   * - ``Dwdt``
     - ``single``
   * - ``Lfdnr``
     - ``int32``
   * - ``Idreferenz``
     - ``string``
   * - ``TypeDescription``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.Fkswvt``
     - ``string``
   * - ``bz.Fkrcpl``
     - ``string``
   * - ``bz.Wsostd``
     - ``single``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``MAINELEMENT``
   * - ``RCPL``
   * - ``SWVT``
   * - ``W``

RCPL
^^^^
Object Type: ``ControlPointTable``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Aktiv``
     - ``int32``
   * - ``Typ``
     - ``int32``
   * - ``Idreferenz``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``KNOT``
   * - ``MAINELEMENT``
   * - ``W``
   * - ``X``
   * - ``XD``

RCPL_ROWT
^^^^^^^^^
Object Type: ``ControlPointTable_Row``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Fk``
     - ``string``
   * - ``Fkkref1``
     - ``string``
   * - ``Fkkref2``
     - ``string``
   * - ``W``
     - ``single``
   * - ``Aktiv``
     - ``int32``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``MAINELEMENT``
   * - ``W``
   * - ``X``
   * - ``XD``

REGV
^^^^
Object Type: ``ControlValve``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Dn``
     - ``single``
   * - ``Fkzep1``
     - ``string``
   * - ``Fkcont``
     - ``string``
   * - ``Thub``
     - ``single``
   * - ``Idreferenz``
     - ``string``
   * - ``Iplanung``
     - ``int32``
   * - ``OnlStrgString``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``ShowDescription``
     - ``boolean``
   * - ``PositionOfDescription``
     - ``int32``
   * - ``Angle``
     - ``double``
   * - ``SymbolFactor``
     - ``double``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.Fkrart``
     - ``string``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``DH``
   * - ``DP``
   * - ``DPH``
   * - ``DSI``
   * - ``DSK``
   * - ``FS``
   * - ``HR``
   * - ``IAKTIV``
   * - ``INDSTD``
   * - ``KV``
   * - ``M``
   * - ``MAINELEMENT``
   * - ``PHI``
   * - ``PR``
   * - ``Q2``
   * - ``QM``
   * - ``RART``
   * - ``RHO``
   * - ``V``
   * - ``W``
   * - ``X``
   * - ``ZETA``

RSTN
^^^^
Object Type: ``ControlVariableConverter``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Ka``
     - ``string``
   * - ``Ityp``
     - ``int32``
   * - ``Typ``
     - ``string``
   * - ``Ymin``
     - ``single``
   * - ``Ymax``
     - ``single``
   * - ``Ys1``
     - ``single``
   * - ``Ys2``
     - ``single``
   * - ``Indyno``
     - ``int32``
   * - ``Dsdt``
     - ``single``
   * - ``Fkvent``
     - ``string``
   * - ``Fkpreg``
     - ``string``
   * - ``Fkdprg``
     - ``string``
   * - ``Fkmreg``
     - ``string``
   * - ``Fkfwes``
     - ``string``
   * - ``Fkfwwu``
     - ``string``
   * - ``Fkrart``
     - ``string``
   * - ``Fkpgrp``
     - ``string``
   * - ``Fkregv``
     - ``string``
   * - ``Fkknot``
     - ``string``
   * - ``Fkrohr``
     - ``string``
   * - ``Fkpump``
     - ``string``
   * - ``Fkobeh``
     - ``string``
   * - ``Fkkomp``
     - ``string``
   * - ``Fkgvwk``
     - ``string``
   * - ``Fkpumppg``
     - ``string``
   * - ``Fkrartpg``
     - ``string``
   * - ``Fkcont``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``AnalogInputE1``
     - ``string``
   * - ``LogicalInputE2``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``RglSymbolTyp``
     - ``rglsymboltype``
   * - ``SymbolFactor``
     - ``double``
   * - ``Angle``
     - ``double``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.Fklfkt``
     - ``string``
   * - ``bz.Fkphi1``
     - ``string``
   * - ``bz.Fkpumd``
     - ``string``
   * - ``bz.Fktevt``
     - ``string``
   * - ``bz.Fkwevt``
     - ``string``
   * - ``bz.Fkswvt``
     - ``string``
   * - ``bz.Fkpvar``
     - ``string``
   * - ``bz.Fkqvar``
     - ``string``
   * - ``bz.Fkrcpl``
     - ``string``
   * - ``bz.FkrcplRowt``
     - ``string``
   * - ``bz.Iaktiv``
     - ``int32``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``LFKT``
   * - ``MAINELEMENT``
   * - ``PHI1``
   * - ``PUMD``
   * - ``PVAR``
   * - ``QVAR``
   * - ``SWVT``
   * - ``TEVT``
   * - ``TRGCOUNT``
   * - ``WEVT``
   * - ``XE1``
   * - ``XE2``

RSTE
^^^^
Object Type: ``ControlVariableConverterRSTE``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Ka``
     - ``string``
   * - ``Typ1``
     - ``string``
   * - ``Kmes1i``
     - ``string``
   * - ``Kmes1k``
     - ``string``
   * - ``Ymin1``
     - ``single``
   * - ``Ymax1``
     - ``single``
   * - ``Ys11``
     - ``single``
   * - ``Ys21``
     - ``single``
   * - ``Indyno1``
     - ``int32``
   * - ``Dsdt1``
     - ``single``
   * - ``Fkvbel1``
     - ``string``
   * - ``Typ2``
     - ``string``
   * - ``Kmes2i``
     - ``string``
   * - ``Kmes2k``
     - ``string``
   * - ``Ymin2``
     - ``single``
   * - ``Ymax2``
     - ``single``
   * - ``Ys12``
     - ``single``
   * - ``Ys22``
     - ``single``
   * - ``Indyno2``
     - ``int32``
   * - ``Dsdt2``
     - ``single``
   * - ``Fkvbel2``
     - ``string``
   * - ``Typ3``
     - ``string``
   * - ``Kmes3i``
     - ``string``
   * - ``Kmes3k``
     - ``string``
   * - ``Ymin3``
     - ``single``
   * - ``Ymax3``
     - ``single``
   * - ``Ys13``
     - ``single``
   * - ``Ys23``
     - ``single``
   * - ``Indyno3``
     - ``int32``
   * - ``Dsdt3``
     - ``single``
   * - ``Fkvbel3``
     - ``string``
   * - ``Typ4``
     - ``string``
   * - ``Kmes4i``
     - ``string``
   * - ``Kmes4k``
     - ``string``
   * - ``Ymin4``
     - ``single``
   * - ``Ymax4``
     - ``single``
   * - ``Ys14``
     - ``single``
   * - ``Ys24``
     - ``single``
   * - ``Indyno4``
     - ``int32``
   * - ``Dsdt4``
     - ``single``
   * - ``Fkvbel4``
     - ``string``
   * - ``Typ5``
     - ``string``
   * - ``Kmes5i``
     - ``string``
   * - ``Kmes5k``
     - ``string``
   * - ``Ymin5``
     - ``single``
   * - ``Ymax5``
     - ``single``
   * - ``Ys15``
     - ``single``
   * - ``Ys25``
     - ``single``
   * - ``Indyno5``
     - ``int32``
   * - ``Dsdt5``
     - ``single``
   * - ``Fkvbel5``
     - ``string``
   * - ``Fkcont``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``RglSymbolTyp``
     - ``rglsymboltype``
   * - ``SymbolFactor``
     - ``double``
   * - ``Angle``
     - ``double``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``bz.Fk``
     - ``string``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``DYDT1``
   * - ``DYDT2``
   * - ``DYDT3``
   * - ``DYDT4``
   * - ``DYDT5``
   * - ``MAINELEMENT``
   * - ``XE1``
   * - ``YS1``
   * - ``YS2``
   * - ``YS3``
   * - ``YS4``
   * - ``YS5``

AVOS
^^^^
Object Type: ``CrossSectionTable``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Zeitoption``
     - ``int32``

Result Properties
"""""""""""""""""

No result properties found.

AVOS_ROWS
^^^^^^^^^
Object Type: ``CrossSectionTable_Row``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Fk``
     - ``string``
   * - ``Ordinate``
     - ``single``
   * - ``Flaeche``
     - ``single``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

No result properties found.

DPGR_DPKT
^^^^^^^^^
Object Type: ``DPGR_DPKT_DatapointDpgrConnection``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Fkdpgr``
     - ``string``
   * - ``Fkdpkt``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

No result properties found.

DPGR
^^^^
Object Type: ``DPGR_DataPointGroup``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``PermissionFlags``
     - ``int32``
   * - ``Typ``
     - ``int32``
   * - ``Dtfak``
     - ``int32``
   * - ``OpcgroupName``
     - ``string``
   * - ``OpcserverPath``
     - ``string``
   * - ``Description``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.LocalUse``
     - ``int32``
   * - ``bz.ExternalUse``
     - ``int32``

Result Properties
"""""""""""""""""

No result properties found.

DPKT
^^^^
Object Type: ``DPKT_Datapoint``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Objtype``
     - ``string``
   * - ``Attrtype``
     - ``string``
   * - ``Epkz``
     - ``int32``
   * - ``Title``
     - ``string``
   * - ``Unit``
     - ``string``
   * - ``Flags``
     - ``int32``
   * - ``Ol3command``
     - ``string``
   * - ``Datatype``
     - ``string``
   * - ``Datalength``
     - ``int32``
   * - ``Description``
     - ``string``
   * - ``Name1``
     - ``string``
   * - ``Name2``
     - ``string``
   * - ``Name3``
     - ``string``
   * - ``Fkobjtype``
     - ``string``
   * - ``ClientId``
     - ``string``
   * - ``OpcitemId``
     - ``string``
   * - ``ClientFlags``
     - ``int32``
   * - ``Factor``
     - ``single``
   * - ``Addend``
     - ``single``
   * - ``Deviation``
     - ``single``
   * - ``LowerLimit``
     - ``single``
   * - ``UpperLimit``
     - ``single``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.Name1``
     - ``string``
   * - ``bz.Name2``
     - ``string``
   * - ``bz.Name3``
     - ``string``
   * - ``bz.Fkobjtype``
     - ``string``
   * - ``bz.ClientId``
     - ``string``
   * - ``bz.OpcitemId``
     - ``string``
   * - ``bz.ClientFlags``
     - ``int32``
   * - ``bz.Factor``
     - ``single``
   * - ``bz.Addend``
     - ``single``
   * - ``bz.Deviation``
     - ``single``
   * - ``bz.CheckAll``
     - ``int32``
   * - ``bz.CheckMsg``
     - ``int32``
   * - ``bz.CheckAbs``
     - ``int32``
   * - ``bz.LowerLimit``
     - ``single``
   * - ``bz.UpperLimit``
     - ``single``
   * - ``bz.LimitToler``
     - ``single``

Result Properties
"""""""""""""""""

No result properties found.

SRAT
^^^^
Object Type: ``DamageRatesTable``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Zeitoption``
     - ``int32``

Result Properties
"""""""""""""""""

No result properties found.

SRAT_ROWS
^^^^^^^^^
Object Type: ``DamageRatesTable_Row``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Fk``
     - ``string``
   * - ``Ralter``
     - ``int32``
   * - ``Srate``
     - ``single``
   * - ``Erate``
     - ``single``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

No result properties found.

RTOT
^^^^
Object Type: ``DeadTimeElement``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Ka``
     - ``string``
   * - ``Ttot``
     - ``single``
   * - ``Fkcont``
     - ``string``
   * - ``E1``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``RglSymbolTyp``
     - ``rglsymboltype``
   * - ``SymbolFactor``
     - ``double``
   * - ``Angle``
     - ``double``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``bz.Fk``
     - ``string``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``MAINELEMENT``
   * - ``XA``
   * - ``XE``

VERB
^^^^
Object Type: ``Demand``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Betriebsstatus``
     - ``int32``
   * - ``ErzeugungArt``
     - ``int32``
   * - ``ErzeugungInfo``
     - ``string``
   * - ``Verbrauch``
     - ``double``
   * - ``VerbrauchDatum``
     - ``string``
   * - ``Fkhaus``
     - ``string``
   * - ``Zkor``
     - ``single``
   * - ``ZaehlerId``
     - ``string``
   * - ``KundenId``
     - ``string``
   * - ``Dimension``
     - ``string``
   * - ``Spartentyp``
     - ``string``
   * - ``Kundengruppe``
     - ``string``
   * - ``Tariftyp``
     - ``string``
   * - ``Betriebsstunden``
     - ``single``
   * - ``Jahresarbeit``
     - ``single``
   * - ``Warmwasserleistung``
     - ``single``
   * - ``Heizleistung``
     - ``single``
   * - ``Kuehlleistung``
     - ``single``
   * - ``Sonstige``
     - ``single``
   * - ``Tvl0``
     - ``single``
   * - ``Trs0``
     - ``single``
   * - ``MengenbegrHwd``
     - ``single``
   * - ``Hausanlagentyp``
     - ``string``
   * - ``Hausanlagenbauart``
     - ``string``
   * - ``Pvl``
     - ``single``
   * - ``Prl``
     - ``single``
   * - ``Qhm``
     - ``single``
   * - ``QhmaxFh``
     - ``single``
   * - ``QhmaxFd``
     - ``single``
   * - ``LaengeHal``
     - ``single``
   * - ``LaengeHauseinfuehrung``
     - ``single``
   * - ``Rau``
     - ``single``
   * - ``Zeta``
     - ``single``
   * - ``Idreferenz``
     - ``string``
   * - ``AenderungArt``
     - ``int32``
   * - ``AenderungInfo``
     - ``string``
   * - ``AenderungDatum``
     - ``string``
   * - ``Hausnr``
     - ``int32``
   * - ``HausnrZus``
     - ``string``
   * - ``Plz``
     - ``int32``
   * - ``ViewX``
     - ``double``
   * - ``ViewY``
     - ``double``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``Graphics``
     - ``hausverbgraf``
   * - ``bz.Fk``
     - ``string``

Result Properties
"""""""""""""""""

No result properties found.

DPRG
^^^^
Object Type: ``DifferentialRegulator``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Dn``
     - ``single``
   * - ``Typ``
     - ``int32``
   * - ``Fkkref1``
     - ``string``
   * - ``Fkkref2``
     - ``string``
   * - ``Fkzep1``
     - ``string``
   * - ``Ts``
     - ``single``
   * - ``Fkcont``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``Iplanung``
     - ``int32``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``ShowDescription``
     - ``boolean``
   * - ``PositionOfDescription``
     - ``int32``
   * - ``Angle``
     - ``double``
   * - ``SymbolFactor``
     - ``double``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.Fkswvt``
     - ``string``
   * - ``bz.Dphsoll``
     - ``single``
   * - ``bz.Indsoll``
     - ``int32``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``DH``
   * - ``DP``
   * - ``DPH``
   * - ``DPHSOLL``
   * - ``DPSOLL``
   * - ``DSI``
   * - ``DSK``
   * - ``FS``
   * - ``HR``
   * - ``IAKTIV``
   * - ``KV``
   * - ``M``
   * - ``MAINELEMENT``
   * - ``PHI``
   * - ``PR``
   * - ``QM``
   * - ``RHO``
   * - ``SWVT``
   * - ``V``
   * - ``ZETA``

RPFL
^^^^
Object Type: ``DirectionalArrow``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Fkcont``
     - ``string``
   * - ``FkdpgrDpkt``
     - ``string``
   * - ``Inddir``
     - ``int32``
   * - ``Beschreibung``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``LineWidthMM``
     - ``double``
   * - ``LineColor``
     - ``color``
   * - ``FillColor``
     - ``color``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``SymbolFactor``
     - ``double``
   * - ``Angle``
     - ``double``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.Eps``
     - ``single``

Result Properties
"""""""""""""""""

No result properties found.

FWVB
^^^^
Object Type: ``DistrictHeatingConsumer``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``Unknown``
   * - ``Beschreibung``
     - ``Unknown``
   * - ``Ind0``
     - ``Unknown``
   * - ``W0``
     - ``Unknown``
   * - ``Qm0``
     - ``Unknown``
   * - ``Tvl0``
     - ``Unknown``
   * - ``Trs0``
     - ``Unknown``
   * - ``Lfk``
     - ``Unknown``
   * - ``Rho0``
     - ``Unknown``
   * - ``Dtmin``
     - ``Unknown``
   * - ``Indtr``
     - ``Unknown``
   * - ``Trsk``
     - ``Unknown``
   * - ``Fktrft``
     - ``Unknown``
   * - ``A``
     - ``Unknown``
   * - ``B``
     - ``Unknown``
   * - ``C``
     - ``Unknown``
   * - ``Vtyp``
     - ``Unknown``
   * - ``V0``
     - ``Unknown``
   * - ``P1soll``
     - ``Unknown``
   * - ``Dpvlmin``
     - ``Unknown``
   * - ``Fkzep1vl``
     - ``Unknown``
   * - ``Tsvl``
     - ``Unknown``
   * - ``Zevk``
     - ``Unknown``
   * - ``Dphaus``
     - ``Unknown``
   * - ``Dprlmin``
     - ``Unknown``
   * - ``Fkzep1rl``
     - ``Unknown``
   * - ``Tsrl``
     - ``Unknown``
   * - ``Imbg``
     - ``Unknown``
   * - ``Irfv``
     - ``Unknown``
   * - ``Fkcont``
     - ``Unknown``
   * - ``Idreferenz``
     - ``Unknown``
   * - ``Iplanung``
     - ``Unknown``
   * - ``CPM``
     - ``Unknown``
   * - ``NumberOfVERB``
     - ``Unknown``
   * - ``IndtrKlartext``
     - ``Unknown``
   * - ``M0Estimated``
     - ``Unknown``
   * - ``W0Estimated``
     - ``Unknown``
   * - ``Tk``
     - ``Unknown``
   * - ``Pk``
     - ``Unknown``
   * - ``InVariant``
     - ``Unknown``
   * - ``Xkor``
     - ``Unknown``
   * - ``Ykor``
     - ``Unknown``
   * - ``ShowDescription``
     - ``Unknown``
   * - ``PositionOfDescription``
     - ``Unknown``
   * - ``Angle``
     - ``Unknown``
   * - ``SymbolFactor``
     - ``Unknown``
   * - ``GeometriesDiffer``
     - ``Unknown``
   * - ``bz.Fk``
     - ``Unknown``
   * - ``bz.Indlast``
     - ``Unknown``
   * - ``bz.Indlfkt2``
     - ``Unknown``
   * - ``bz.Fklfkt``
     - ``Unknown``
   * - ``bz.Fklfkt2``
     - ``Unknown``
   * - ``bz.Fkqvar``
     - ``Unknown``
   * - ``bz.Fktevt``
     - ``Unknown``
   * - ``bz.IndlastKlartext``
     - ``Unknown``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``DH``
   * - ``DP``
   * - ``DPH``
   * - ``IAKTIV``
   * - ``INDUV``
   * - ``LFH``
   * - ``LFKT``
   * - ``LFT``
   * - ``M``
   * - ``MAINELEMENT``
   * - ``MHYUV``
   * - ``MSOLL``
   * - ``MTHUV``
   * - ``P1``
   * - ``P2``
   * - ``P3``
   * - ``PH1``
   * - ``PH2``
   * - ``PH3``
   * - ``PHIRL``
   * - ``PHIVL``
   * - ``QM``
   * - ``QM13``
   * - ``QM31``
   * - ``QMI``
   * - ``QMK``
   * - ``QVAR``
   * - ``RHOI``
   * - ``RHOK``
   * - ``TI``
   * - ``TK``
   * - ``TVMIN``
   * - ``W``
   * - ``WHYUV``
   * - ``WSOLL``
   * - ``WTHUV``

FWES
^^^^
Object Type: ``DistrictHeatingFeeder``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``Unknown``
   * - ``Beschreibung``
     - ``Unknown``
   * - ``Dn``
     - ``Unknown``
   * - ``Zeta``
     - ``Unknown``
   * - ``Taus``
     - ``Unknown``
   * - ``Irueck``
     - ``Unknown``
   * - ``Fkcont``
     - ``Unknown``
   * - ``Idreferenz``
     - ``Unknown``
   * - ``Iplanung``
     - ``Unknown``
   * - ``Tk``
     - ``Unknown``
   * - ``Pk``
     - ``Unknown``
   * - ``InVariant``
     - ``Unknown``
   * - ``Xkor``
     - ``Unknown``
   * - ``Ykor``
     - ``Unknown``
   * - ``ShowDescription``
     - ``Unknown``
   * - ``PositionOfDescription``
     - ``Unknown``
   * - ``Angle``
     - ``Unknown``
   * - ``SymbolFactor``
     - ``Unknown``
   * - ``GeometriesDiffer``
     - ``Unknown``
   * - ``bz.Fk``
     - ``Unknown``
   * - ``bz.Ihytyp``
     - ``Unknown``
   * - ``bz.Ithtyp``
     - ``Unknown``
   * - ``bz.Tkon``
     - ``Unknown``
   * - ``bz.Fktevt``
     - ``Unknown``
   * - ``bz.Wkon``
     - ``Unknown``
   * - ``bz.Fkwevt``
     - ``Unknown``
   * - ``bz.IhytypKlartext``
     - ``Unknown``
   * - ``bz.IthtypKlartext``
     - ``Unknown``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``DH``
   * - ``DP``
   * - ``DPH``
   * - ``IAKTIV``
   * - ``IHYTYP``
   * - ``ITHTYP``
   * - ``M``
   * - ``MAINELEMENT``
   * - ``QM``
   * - ``RHOI``
   * - ``RHOK``
   * - ``TEVT``
   * - ``TI``
   * - ``TK``
   * - ``TKON``
   * - ``V``
   * - ``W``
   * - ``W0``
   * - ``WEVT``
   * - ``WSOLL``

RDIV
^^^^
Object Type: ``Divider``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Ka``
     - ``string``
   * - ``Mindiv``
     - ``single``
   * - ``Inddiv``
     - ``int32``
   * - ``Fkcont``
     - ``string``
   * - ``E1``
     - ``string``
   * - ``E2``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``RglSymbolTyp``
     - ``rglsymboltype``
   * - ``SymbolFactor``
     - ``double``
   * - ``Angle``
     - ``double``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``bz.Fk``
     - ``string``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``MAINELEMENT``
   * - ``XA``
   * - ``XE1``
   * - ``XE2``

ETAM
^^^^
Object Type: ``DriveEfficiencyTable``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Zeitoption``
     - ``int32``

Result Properties
"""""""""""""""""

No result properties found.

ETAM_ROWS
^^^^^^^^^
Object Type: ``DriveEfficiencyTable_Row``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Fk``
     - ``string``
   * - ``Nzun0``
     - ``single``
   * - ``Etam``
     - ``single``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

No result properties found.

ANTP
^^^^
Object Type: ``DrivePowerTable``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Zeitoption``
     - ``int32``

Result Properties
"""""""""""""""""

No result properties found.

ANTP_ROWS
^^^^^^^^^
Object Type: ``DrivePowerTable_Row``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Fk``
     - ``string``
   * - ``Tumg``
     - ``single``
   * - ``Pamax``
     - ``single``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

No result properties found.

EBES
^^^^
Object Type: ``EBES_FeederGroups``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Lfdnr``
     - ``int32``
   * - ``Idreferenz``
     - ``string``
   * - ``ObjsString``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.Aktiv``
     - ``int32``
   * - ``bz.Aktivqs``
     - ``int32``
   * - ``bz.Versagensw``
     - ``single``

Result Properties
"""""""""""""""""

No result properties found.

ETAU
^^^^
Object Type: ``EfficiencyConverterTable``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Zeitoption``
     - ``int32``

Result Properties
"""""""""""""""""

No result properties found.

ETAU_ROWS
^^^^^^^^^
Object Type: ``EfficiencyConverterTable_Row``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Fk``
     - ``string``
   * - ``Nzun0``
     - ``single``
   * - ``Etafu``
     - ``single``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

No result properties found.

ELEMENTQUERY
^^^^^^^^^^^^
Object Type: ``ElementQuery``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Elementtype``
     - ``string``
   * - ``Aktiv``
     - ``int32``
   * - ``Lfdnr``
     - ``int32``
   * - ``QueryStringAsString``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

No result properties found.

ETAR
^^^^
Object Type: ``EnergyRecoveryTable``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Zeitoption``
     - ``int32``

Result Properties
"""""""""""""""""

No result properties found.

ETAR_ROWS
^^^^^^^^^
Object Type: ``EnergyRecoveryTable_Row``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Fk``
     - ``string``
   * - ``Nzun0``
     - ``single``
   * - ``Etadt``
     - ``single``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

No result properties found.

UTMP
^^^^
Object Type: ``EnvironmentTemp``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.Indi``
     - ``int32``
   * - ``bz.Tu``
     - ``single``
   * - ``bz.Fktevt``
     - ``string``
   * - ``bz.Fkwttr``
     - ``string``

Result Properties
"""""""""""""""""

No result properties found.

FWBZ
^^^^
Object Type: ``FWBZ_DistrictHeatingReferenceValues``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Lambdabzg``
     - ``single``
   * - ``Rhobzg``
     - ``single``
   * - ``Hgebzg``
     - ``single``
   * - ``Ikotyp``
     - ``int32``
   * - ``Vhausg``
     - ``single``
   * - ``Ahausg``
     - ``single``
   * - ``Arohr``
     - ``single``
   * - ``Zerohr``
     - ``single``
   * - ``Flfwvb``
     - ``single``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

No result properties found.

KLAP
^^^^
Object Type: ``FlapValve``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Dn``
     - ``single``
   * - ``Fkphiv``
     - ``string``
   * - ``Fkzep2``
     - ``string``
   * - ``Ts``
     - ``single``
   * - ``Phie``
     - ``single``
   * - ``Te``
     - ``single``
   * - ``Fkcont``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``Iplanung``
     - ``int32``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``ShowDescription``
     - ``boolean``
   * - ``PositionOfDescription``
     - ``int32``
   * - ``Angle``
     - ``double``
   * - ``SymbolFactor``
     - ``double``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``bz.Fk``
     - ``string``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``DH``
   * - ``DP``
   * - ``DSI``
   * - ``DSK``
   * - ``FS``
   * - ``HR``
   * - ``IAKTIV``
   * - ``KV``
   * - ``M``
   * - ``MAINELEMENT``
   * - ``PHI``
   * - ``PHR``
   * - ``PR``
   * - ``QM``
   * - ``RHO``
   * - ``V``
   * - ``ZETA``

MREG
^^^^
Object Type: ``FlowControlUnit``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Dn``
     - ``single``
   * - ``Fkzep1``
     - ``string``
   * - ``Tsig``
     - ``single``
   * - ``Dqdt``
     - ``single``
   * - ``Tvoll``
     - ``single``
   * - ``Fkcont``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``Iplanung``
     - ``int32``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``ShowDescription``
     - ``boolean``
   * - ``PositionOfDescription``
     - ``int32``
   * - ``Angle``
     - ``double``
   * - ``SymbolFactor``
     - ``double``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.Indsoll``
     - ``int32``
   * - ``bz.Qmsoll``
     - ``single``
   * - ``bz.Fkswvtqm``
     - ``string``
   * - ``bz.Phisoll``
     - ``single``
   * - ``bz.Fkswvtphi``
     - ``string``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``DH``
   * - ``DP``
   * - ``DPH``
   * - ``DSI``
   * - ``DSK``
   * - ``FS``
   * - ``HR``
   * - ``IAKTIV``
   * - ``IND``
   * - ``KV``
   * - ``M``
   * - ``MAINELEMENT``
   * - ``PHI``
   * - ``PHISOLL``
   * - ``PR``
   * - ``Q``
   * - ``QM``
   * - ``QMSOLL``
   * - ``RHO``
   * - ``SWVTPHI``
   * - ``SWVTQM``
   * - ``V``
   * - ``ZETA``

FQPS
^^^^
Object Type: ``FluidQualityParamSet``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Lfdnr``
     - ``int32``
   * - ``Walter``
     - ``single``
   * - ``Temp``
     - ``single``
   * - ``Eisenges``
     - ``single``
   * - ``Eisenfilt``
     - ``single``
   * - ``Sulfat``
     - ``single``
   * - ``Chlorid``
     - ``single``
   * - ``Leitfaeh``
     - ``single``
   * - ``Phwert``
     - ``single``
   * - ``Hs``
     - ``single``
   * - ``Hi``
     - ``single``
   * - ``Rhon``
     - ``single``
   * - ``Mn``
     - ``int32``
   * - ``Indhs``
     - ``int32``
   * - ``Indhi``
     - ``int32``
   * - ``Indrhon``
     - ``int32``
   * - ``Indmn``
     - ``int32``
   * - ``Indtemp``
     - ``int32``
   * - ``Indeisenges``
     - ``int32``
   * - ``Indeisenfilt``
     - ``int32``
   * - ``Indsulfat``
     - ``int32``
   * - ``Indchlorid``
     - ``int32``
   * - ``Indleitfaeh``
     - ``int32``
   * - ``Indphwert``
     - ``int32``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.Fkswvths``
     - ``string``
   * - ``bz.Fkswvthi``
     - ``string``
   * - ``bz.Fkswvtrhon``
     - ``string``
   * - ``bz.Fkswvtmn``
     - ``string``
   * - ``bz.Fkswvttemp``
     - ``string``
   * - ``bz.Fkswvteisenges``
     - ``string``
   * - ``bz.Fkswvteisenfilt``
     - ``string``
   * - ``bz.Fkswvtsulfat``
     - ``string``
   * - ``bz.Fkswvtchlorid``
     - ``string``
   * - ``bz.Fkswvtleitfaeh``
     - ``string``
   * - ``bz.Fkswvtphwert``
     - ``string``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``MAINELEMENT``
   * - ``SWVTCHLORID``
   * - ``SWVTEISENFILT``
   * - ``SWVTEISENGES``
   * - ``SWVTHI``
   * - ``SWVTHS``
   * - ``SWVTLEITFAEH``
   * - ``SWVTMN``
   * - ``SWVTPHWERT``
   * - ``SWVTRHON``
   * - ``SWVTSULFAT``
   * - ``SWVTTEMP``

FQPS_BZ
^^^^^^^
Object Type: ``FluidQualityParamSet_OS``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Fk``
     - ``string``
   * - ``Fkswvths``
     - ``string``
   * - ``Fkswvthi``
     - ``string``
   * - ``Fkswvtrhon``
     - ``string``
   * - ``Fkswvtmn``
     - ``string``
   * - ``Fkswvttemp``
     - ``string``
   * - ``Fkswvteisenges``
     - ``string``
   * - ``Fkswvteisenfilt``
     - ``string``
   * - ``Fkswvtsulfat``
     - ``string``
   * - ``Fkswvtchlorid``
     - ``string``
   * - ``Fkswvtleitfaeh``
     - ``string``
   * - ``Fkswvtphwert``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

No result properties found.

FSTF
^^^^
Object Type: ``FluidThermalPropertyGroup``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Fkstof``
     - ``string``
   * - ``K``
     - ``single``
   * - ``Eps``
     - ``single``
   * - ``Fkgmix``
     - ``string``
   * - ``Indstf``
     - ``int32``
   * - ``Rhonorm``
     - ``single``
   * - ``Tref``
     - ``single``
   * - ``Pref``
     - ``single``
   * - ``Dynvisko``
     - ``single``
   * - ``Isotherm``
     - ``single``
   * - ``Cp``
     - ``single``
   * - ``Gkomp1``
     - ``single``
   * - ``Gkomp2``
     - ``single``
   * - ``Tabdnam``
     - ``string``
   * - ``Dracoeffa``
     - ``single``
   * - ``Dracoeffb``
     - ``single``
   * - ``Dracoeffc``
     - ``single``
   * - ``Idreferenz``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

No result properties found.

FKNL
^^^^
Object Type: ``FreeDuct``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Cdim``
     - ``string``
   * - ``T``
     - ``single``
   * - ``Ualm``
     - ``single``
   * - ``Uwarn``
     - ``single``
   * - ``Owarn``
     - ``single``
   * - ``Oalm``
     - ``single``
   * - ``Showrect``
     - ``int32``
   * - ``Showname``
     - ``int32``
   * - ``Fkcont``
     - ``string``
   * - ``ElementFont``
     - ``c3sfont``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``BoundingRectangle``
     - ``irectangle``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.Fkwtab``
     - ``string``
   * - ``bz.Wert``
     - ``single``
   * - ``bz.Afakt``
     - ``single``
   * - ``bz.Dy``
     - ``single``
   * - ``bz.Dt``
     - ``single``
   * - ``bz.Ityp``
     - ``int32``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``MAINELEMENT``
   * - ``OA``
   * - ``OW``
   * - ``UA``
   * - ``UW``
   * - ``WERT``

RFKT
^^^^
Object Type: ``FunctionGenerator``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Ka``
     - ``string``
   * - ``Indfkt``
     - ``int32``
   * - ``Fktfkt``
     - ``string``
   * - ``Fkcont``
     - ``string``
   * - ``E1``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``RglSymbolTyp``
     - ``rglsymboltype``
   * - ``SymbolFactor``
     - ``double``
   * - ``Angle``
     - ``double``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.Fklfkt``
     - ``string``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``LFKT``
   * - ``MAINELEMENT``
   * - ``XA``
   * - ``XE``

TFKT
^^^^
Object Type: ``FunctionTable``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Zeitoption``
     - ``int32``

Result Properties
"""""""""""""""""

No result properties found.

TFKT_ROWS
^^^^^^^^^
Object Type: ``FunctionTable_Row``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Fk``
     - ``string``
   * - ``X``
     - ``single``
   * - ``Y``
     - ``single``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

No result properties found.

GKMP
^^^^
Object Type: ``GasComponent``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Formula``
     - ``string``
   * - ``Lfdnr``
     - ``int32``
   * - ``Molarmass``
     - ``single``
   * - ``Hs``
     - ``single``
   * - ``Hi``
     - ``single``
   * - ``BwrA0``
     - ``single``
   * - ``BwrB0``
     - ``single``
   * - ``BwrC0``
     - ``single``
   * - ``BwrA``
     - ``single``
   * - ``BwrB``
     - ``single``
   * - ``BwrC``
     - ``single``
   * - ``BwrAlpha``
     - ``single``
   * - ``BwrGamma``
     - ``single``
   * - ``Zisocoef``
     - ``single``
   * - ``CpicoefA``
     - ``single``
   * - ``CpicoefB``
     - ``single``
   * - ``CpicoefC``
     - ``single``
   * - ``CpicoefD``
     - ``single``
   * - ``CpicoefE``
     - ``single``
   * - ``Tb``
     - ``single``
   * - ``Pc``
     - ``single``
   * - ``Tc``
     - ``single``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

No result properties found.

GMIX
^^^^
Object Type: ``GasMixture``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Lfdnr``
     - ``int32``
   * - ``Fkgkmp1``
     - ``string``
   * - ``Molfrac1``
     - ``single``
   * - ``Fkgkmp2``
     - ``string``
   * - ``Molfrac2``
     - ``single``
   * - ``Fkgkmp3``
     - ``string``
   * - ``Molfrac3``
     - ``single``
   * - ``Fkgkmp4``
     - ``string``
   * - ``Molfrac4``
     - ``single``
   * - ``Fkgkmp5``
     - ``string``
   * - ``Molfrac5``
     - ``single``
   * - ``Fkgkmp6``
     - ``string``
   * - ``Molfrac6``
     - ``single``
   * - ``Fkgkmp7``
     - ``string``
   * - ``Molfrac7``
     - ``single``
   * - ``Fkgkmp8``
     - ``string``
   * - ``Molfrac8``
     - ``single``
   * - ``Fkgkmp9``
     - ``string``
   * - ``Molfrac9``
     - ``single``
   * - ``Fkgkmp10``
     - ``string``
   * - ``Molfrac10``
     - ``single``
   * - ``Fkgkmp11``
     - ``string``
   * - ``Molfrac11``
     - ``single``
   * - ``Fkgkmp12``
     - ``string``
   * - ``Molfrac12``
     - ``single``
   * - ``Fkgkmp13``
     - ``string``
   * - ``Molfrac13``
     - ``single``
   * - ``Fkgkmp14``
     - ``string``
   * - ``Molfrac14``
     - ``single``
   * - ``Fkgkmp15``
     - ``string``
   * - ``Molfrac15``
     - ``single``
   * - ``Fkgkmp16``
     - ``string``
   * - ``Molfrac16``
     - ``single``
   * - ``Fkgkmp17``
     - ``string``
   * - ``Molfrac17``
     - ``single``
   * - ``Fkgkmp18``
     - ``string``
   * - ``Molfrac18``
     - ``single``
   * - ``Fkgkmp19``
     - ``string``
   * - ``Molfrac19``
     - ``single``
   * - ``Fkgkmp20``
     - ``string``
   * - ``Molfrac20``
     - ``single``
   * - ``Fkgkmp21``
     - ``string``
   * - ``Molfrac21``
     - ``single``
   * - ``Fkgkmp22``
     - ``string``
   * - ``Molfrac22``
     - ``single``
   * - ``Idreferenz``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

No result properties found.

ALLG
^^^^
Object Type: ``GeneralSection``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Idqm``
     - ``int32``
   * - ``Idph``
     - ``int32``
   * - ``Netztyp``
     - ``int32``
   * - ``Forc``
     - ``int32``
   * - ``Pfadol1``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.Cdat``
     - ``string``
   * - ``bz.Cuhr``
     - ``string``
   * - ``bz.Czon``
     - ``string``
   * - ``bz.Iart``
     - ``int32``
   * - ``bz.ArtTh``
     - ``int32``
   * - ``bz.Thfakt``
     - ``int32``
   * - ``bz.Itrenn``
     - ``int32``
   * - ``bz.ThStat``
     - ``int32``
   * - ``bz.ThInst``
     - ``int32``
   * - ``bz.Jwarn``
     - ``int32``
   * - ``bz.Lfqsv``
     - ``single``
   * - ``bz.Schwellqsig``
     - ``single``
   * - ``bz.Knuvtyp``
     - ``int32``
   * - ``bz.ValidAggr``
     - ``int32``
   * - ``bz.CalcNetwork``
     - ``int32``
   * - ``bz.Idra``
     - ``int32``
   * - ``bz.CheckRes``
     - ``int32``
   * - ``bz.CheckMod``
     - ``int32``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``CPUTIME``
   * - ``CVERSO``
   * - ``EXSTAT``
   * - ``FWVB_DPHMIN``
   * - ``FWVB_TVLMIN``
   * - ``INTERAKTRG``
   * - ``INTERAKTTH``
   * - ``ITERHY``
   * - ``ITERTH``
   * - ``JWARN``
   * - ``KNOT_PHMAX``
   * - ``KNOT_PHMAX_R``
   * - ``KNOT_PHMAX_U``
   * - ``KNOT_PHMAX_V``
   * - ``KNOT_PHMIN``
   * - ``KNOT_PHMIN_R``
   * - ``KNOT_PHMIN_U``
   * - ``KNOT_PHMIN_V``
   * - ``LFQSV``
   * - ``LINEPACKGEOM``
   * - ``LINEPACKGES``
   * - ``LINEPACKRATE``
   * - ``MAINELEMENT``
   * - ``MFVHYUV``
   * - ``MFVTHUV``
   * - ``MKNUV``
   * - ``NETZABN``
   * - ``NETZABNEXITS``
   * - ``NETZBEZ``
   * - ``NFEHL``
   * - ``NFVHYUV``
   * - ``NFVTHUV``
   * - ``NKNUV``
   * - ``NMELD``
   * - ``NPGREST``
   * - ``NWARN``
   * - ``PAV``
   * - ``RHOAV``
   * - ``SNAPSHOTTYPE``
   * - ``TAV``
   * - ``TIMESTAMP``
   * - ``TVMINMAX``
   * - ``USRTIME``

GRAV
^^^^
Object Type: ``Gravitation``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Jgrav``
     - ``int32``
   * - ``Beschx``
     - ``single``
   * - ``Beschy``
     - ``single``
   * - ``Beschz``
     - ``single``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

No result properties found.

FWWU
^^^^
Object Type: ``HeatExchanger``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``Unknown``
   * - ``Beschreibung``
     - ``Unknown``
   * - ``W0``
     - ``Unknown``
   * - ``T1ein0``
     - ``Unknown``
   * - ``T1aus0``
     - ``Unknown``
   * - ``T2ein0``
     - ``Unknown``
   * - ``T2aus0``
     - ``Unknown``
   * - ``Dn``
     - ``Unknown``
   * - ``Dp10min``
     - ``Unknown``
   * - ``Inddprl``
     - ``Unknown``
   * - ``Fkzep1rl``
     - ``Unknown``
   * - ``Tsrl``
     - ``Unknown``
   * - ``Dp20``
     - ``Unknown``
   * - ``Re0``
     - ``Unknown``
   * - ``Expert``
     - ``Unknown``
   * - ``A``
     - ``Unknown``
   * - ``K``
     - ``Unknown``
   * - ``Alpha1``
     - ``Unknown``
   * - ``Alpha2``
     - ``Unknown``
   * - ``L1``
     - ``Unknown``
   * - ``L2``
     - ``Unknown``
   * - ``Indwue``
     - ``Unknown``
   * - ``Kstrant``
     - ``Unknown``
   * - ``Fkfwvb``
     - ``Unknown``
   * - ``Fkfwes``
     - ``Unknown``
   * - ``Fkcont``
     - ``Unknown``
   * - ``Idreferenz``
     - ``Unknown``
   * - ``Iplanung``
     - ``Unknown``
   * - ``Tk``
     - ``Unknown``
   * - ``Pk``
     - ``Unknown``
   * - ``InVariant``
     - ``Unknown``
   * - ``Xkor``
     - ``Unknown``
   * - ``Ykor``
     - ``Unknown``
   * - ``ShowDescription``
     - ``Unknown``
   * - ``PositionOfDescription``
     - ``Unknown``
   * - ``Angle``
     - ``Unknown``
   * - ``SymbolFactor``
     - ``Unknown``
   * - ``GeometriesDiffer``
     - ``Unknown``
   * - ``bz.Fk``
     - ``Unknown``
   * - ``bz.Einaus``
     - ``Unknown``
   * - ``bz.Ithtyp``
     - ``Unknown``
   * - ``bz.T2aus``
     - ``Unknown``
   * - ``bz.Fktevt``
     - ``Unknown``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``AKTIV``
   * - ``C1``
   * - ``C2``
   * - ``EPS1``
   * - ``EPS2``
   * - ``IAKTIV``
   * - ``INDUV``
   * - ``KA``
   * - ``MAINELEMENT``
   * - ``NTU1``
   * - ``NTU2``
   * - ``NU1``
   * - ``NU2``
   * - ``PR1``
   * - ``PR2``
   * - ``Q``
   * - ``RE1``
   * - ``RE2``
   * - ``T1AUS``
   * - ``T1EIN``
   * - ``T2AUS``
   * - ``T2EIN``
   * - ``THETA``
   * - ``TMLOG``
   * - ``W1``
   * - ``W2``

FWEA
^^^^
Object Type: ``HeatFeederConsumerStation``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``Unknown``
   * - ``Beschreibung``
     - ``Unknown``
   * - ``Fkfwes``
     - ``Unknown``
   * - ``Fkfwvb``
     - ``Unknown``
   * - ``Fkpreg``
     - ``Unknown``
   * - ``Fkpump``
     - ``Unknown``
   * - ``Fkklap``
     - ``Unknown``
   * - ``Indusing``
     - ``Unknown``
   * - ``Dn``
     - ``Unknown``
   * - ``Dpvb0min``
     - ``Unknown``
   * - ``Dpes0``
     - ``Unknown``
   * - ``PuQmref``
     - ``Unknown``
   * - ``PuNref``
     - ``Unknown``
   * - ``PuHref``
     - ``Unknown``
   * - ``PuPref``
     - ``Unknown``
   * - ``Volsp``
     - ``Unknown``
   * - ``HMantel``
     - ``Unknown``
   * - ``HWsOkDif``
     - ``Unknown``
   * - ``HDif``
     - ``Unknown``
   * - ``HBUkDif``
     - ``Unknown``
   * - ``RInnen``
     - ``Unknown``
   * - ``RDif``
     - ``Unknown``
   * - ``HWsMax``
     - ``Unknown``
   * - ``Dhbasis``
     - ``Unknown``
   * - ``UMantel``
     - ``Unknown``
   * - ``UBoden``
     - ``Unknown``
   * - ``Tob``
     - ``Unknown``
   * - ``Tu``
     - ``Unknown``
   * - ``Tdr``
     - ``Unknown``
   * - ``TrefMin``
     - ``Unknown``
   * - ``TtolEs``
     - ``Unknown``
   * - ``TtolVb``
     - ``Unknown``
   * - ``W0Sp``
     - ``Unknown``
   * - ``W0Es``
     - ``Unknown``
   * - ``Tsp0``
     - ``Unknown``
   * - ``Trl0``
     - ``Unknown``
   * - ``W0Vb``
     - ``Unknown``
   * - ``Tvl0``
     - ``Unknown``
   * - ``Trs0``
     - ``Unknown``
   * - ``Indtr``
     - ``Unknown``
   * - ``Fktrft``
     - ``Unknown``
   * - ``Fksoko``
     - ``Unknown``
   * - ``Indtrack``
     - ``Unknown``
   * - ``Medium``
     - ``Unknown``
   * - ``Qfs``
     - ``Unknown``
   * - ``Tgrenz``
     - ``Unknown``
   * - ``Deta0bLost``
     - ``Unknown``
   * - ``Abrutto``
     - ``Unknown``
   * - ``Wcorr``
     - ``Unknown``
   * - ``Indrohr``
     - ``Unknown``
   * - ``Vrv``
     - ``Unknown``
   * - ``Indrumg``
     - ``Unknown``
   * - ``L``
     - ``Unknown``
   * - ``Di``
     - ``Unknown``
   * - ``Kr``
     - ``Unknown``
   * - ``Rd``
     - ``Unknown``
   * - ``Lambdad``
     - ``Unknown``
   * - ``Lambdae``
     - ``Unknown``
   * - ``He``
     - ``Unknown``
   * - ``KrKt``
     - ``Unknown``
   * - ``Tru``
     - ``Unknown``
   * - ``Indwt``
     - ``Unknown``
   * - ``Dtwt``
     - ``Unknown``
   * - ``Indtset``
     - ``Unknown``
   * - ``Gtmaxtset``
     - ``Unknown``
   * - ``Dtsett``
     - ``Unknown``
   * - ``PrDn``
     - ``Unknown``
   * - ``Fkzep1Pr``
     - ``Unknown``
   * - ``Fkcont``
     - ``Unknown``
   * - ``Idreferenz``
     - ``Unknown``
   * - ``Iplanung``
     - ``Unknown``
   * - ``NodeNameI``
     - ``Unknown``
   * - ``NodeNameK``
     - ``Unknown``
   * - ``StorageType``
     - ``Unknown``
   * - ``Tk``
     - ``Unknown``
   * - ``Pk``
     - ``Unknown``
   * - ``InVariant``
     - ``Unknown``
   * - ``Xkor``
     - ``Unknown``
   * - ``Ykor``
     - ``Unknown``
   * - ``ShowDescription``
     - ``Unknown``
   * - ``PositionOfDescription``
     - ``Unknown``
   * - ``Angle``
     - ``Unknown``
   * - ``SymbolFactor``
     - ``Unknown``
   * - ``GeometriesDiffer``
     - ``Unknown``
   * - ``bz.Fk``
     - ``Unknown``
   * - ``bz.Einaus``
     - ``Unknown``
   * - ``bz.IndsSp``
     - ``Unknown``
   * - ``bz.ModeSp``
     - ``Unknown``
   * - ``bz.Ithtyp``
     - ``Unknown``
   * - ``bz.Indlast``
     - ``Unknown``
   * - ``bz.Neigung``
     - ``Unknown``
   * - ``bz.Azimut``
     - ``Unknown``
   * - ``bz.Fkwttr``
     - ``Unknown``
   * - ``bz.FktevtEs``
     - ``Unknown``
   * - ``bz.FktevtRs``
     - ``Unknown``
   * - ``bz.FkwevtSp``
     - ``Unknown``
   * - ``bz.FkqvarSp``
     - ``Unknown``
   * - ``bz.FkwevtEs``
     - ``Unknown``
   * - ``bz.FkwevtVb``
     - ``Unknown``
   * - ``bz.Fklfkt``
     - ``Unknown``
   * - ``bz.Pvlmax``
     - ``Unknown``
   * - ``bz.Ppumax``
     - ``Unknown``
   * - ``bz.Indstagn``
     - ``Unknown``
   * - ``bz.TzuMax``
     - ``Unknown``
   * - ``bz.TzuMin``
     - ``Unknown``
   * - ``bz.TspMin``
     - ``Unknown``
   * - ``bz.TrsMax``
     - ``Unknown``
   * - ``bz.W0SpMin``
     - ``Unknown``
   * - ``bz.Qsprel0``
     - ``Unknown``
   * - ``bz.HWsStart``
     - ``Unknown``
   * - ``bz.TobStart``
     - ``Unknown``
   * - ``bz.TuStart``
     - ``Unknown``
   * - ``bz.TtolEval``
     - ``Unknown``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``DH_KALT``
   * - ``DH_MIX``
   * - ``DH_WARM``
   * - ``DPH_ES``
   * - ``DPH_VB``
   * - ``DTLEER``
   * - ``ETA_PU``
   * - ``GGLOB``
   * - ``GKOLL``
   * - ``H_MIX``
   * - ``H_PU``
   * - ``H_WS``
   * - ``IAKTIV``
   * - ``MAINELEMENT``
   * - ``MMAXBL``
   * - ``MMAXEL``
   * - ``MMIN``
   * - ``N_PU``
   * - ``P_PU``
   * - ``Q_PU``
   * - ``QM``
   * - ``QM_ES``
   * - ``QM_PR``
   * - ``QM_VB``
   * - ``QSP``
   * - ``QSPREL``
   * - ``QV_BODEN``
   * - ``QV_DR``
   * - ``QV_MANTEL``
   * - ``QV_TOTAL``
   * - ``T_KALT``
   * - ``T_MIX``
   * - ``T_WARM``
   * - ``TDIFFO``
   * - ``TDIFFU``
   * - ``TRL``
   * - ``TRS``
   * - ``TSP``
   * - ``TVEC``
   * - ``TVL``
   * - ``W``
   * - ``W_ES``
   * - ``W_FS``
   * - ``W_PR``
   * - ``W_RO``
   * - ``W_VB``
   * - ``WKOLL``

GVWK
^^^^
Object Type: ``HeaterCooler``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``Unknown``
   * - ``Beschreibung``
     - ``Unknown``
   * - ``Eta``
     - ``Unknown``
   * - ``Dpnum``
     - ``Unknown``
   * - ``Fkcont``
     - ``Unknown``
   * - ``Idreferenz``
     - ``Unknown``
   * - ``Iplanung``
     - ``Unknown``
   * - ``Tk``
     - ``Unknown``
   * - ``Pk``
     - ``Unknown``
   * - ``InVariant``
     - ``Unknown``
   * - ``Xkor``
     - ``Unknown``
   * - ``Ykor``
     - ``Unknown``
   * - ``ShowDescription``
     - ``Unknown``
   * - ``PositionOfDescription``
     - ``Unknown``
   * - ``Angle``
     - ``Unknown``
   * - ``SymbolFactor``
     - ``Unknown``
   * - ``GeometriesDiffer``
     - ``Unknown``
   * - ``bz.Fk``
     - ``Unknown``
   * - ``bz.Inds``
     - ``Unknown``
   * - ``bz.Sw``
     - ``Unknown``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``EINAUS``
   * - ``IAKTIV``
   * - ``M``
   * - ``MAINELEMENT``
   * - ``P``
   * - ``PE``
   * - ``PI``
   * - ``PK``
   * - ``QN``
   * - ``TI``
   * - ``TK``

RHYS
^^^^
Object Type: ``Histeresis``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Ka``
     - ``string``
   * - ``Xu``
     - ``single``
   * - ``Xo``
     - ``single``
   * - ``Xstart``
     - ``single``
   * - ``Indhys``
     - ``int32``
   * - ``Fkcont``
     - ``string``
   * - ``E1``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``RglSymbolTyp``
     - ``rglsymboltype``
   * - ``SymbolFactor``
     - ``double``
   * - ``Angle``
     - ``double``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``bz.Fk``
     - ``string``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``MAINELEMENT``
   * - ``XA``
   * - ``XE``
   * - ``XO``
   * - ``XU``

HAUS
^^^^
Object Type: ``House``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Fkstrasse``
     - ``string``
   * - ``Fkknot``
     - ``string``
   * - ``Fkfwvb``
     - ``string``
   * - ``Hausnr``
     - ``int32``
   * - ``HausnrZus``
     - ``string``
   * - ``Plz``
     - ``int32``
   * - ``DsnBundesweit``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``TotalDemand``
     - ``double``
   * - ``ViewX``
     - ``double``
   * - ``ViewY``
     - ``double``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``SymbolFactor``
     - ``double``
   * - ``Graphics``
     - ``hausverbgraf``
   * - ``bz.Fk``
     - ``string``

Result Properties
"""""""""""""""""

No result properties found.

HYDR
^^^^
Object Type: ``Hydrant``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Typ``
     - ``int32``
   * - ``Zkor``
     - ``single``
   * - ``Zeta``
     - ``single``
   * - ``Dn``
     - ``single``
   * - ``FkdtroRowd``
     - ``string``
   * - ``L``
     - ``single``
   * - ``Rau``
     - ``single``
   * - ``Fkrohr``
     - ``string``
   * - ``Poskm``
     - ``single``
   * - ``Fkknot``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``Angle``
     - ``double``
   * - ``SymbolFactor``
     - ``double``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.Phsoll``
     - ``single``
   * - ``bz.Qmsoll``
     - ``single``
   * - ``bz.Indi``
     - ``int32``
   * - ``bz.Iaktiv``
     - ``int32``
   * - ``bz.Fkswvt``
     - ``string``
   * - ``bz.PhMin``
     - ``single``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``BCTYP``
   * - ``IAKTIV``
   * - ``MAINELEMENT``
   * - ``PH_EINB``
   * - ``PH_ENTN``
   * - ``PH_MIN``
   * - ``PHR``
   * - ``PHR_ROHR``
   * - ``PHSOLL``
   * - ``QM``
   * - ``QSOLL``
   * - ``UV``

RINT
^^^^
Object Type: ``Integrator``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Ka``
     - ``string``
   * - ``Ugr``
     - ``single``
   * - ``Ogr``
     - ``single``
   * - ``Fkcont``
     - ``string``
   * - ``E1``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``RglSymbolTyp``
     - ``rglsymboltype``
   * - ``SymbolFactor``
     - ``double``
   * - ``Angle``
     - ``double``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``bz.Fk``
     - ``string``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``MAINELEMENT``
   * - ``XA``
   * - ``XE``

LAYR
^^^^
Object Type: ``LAYR_Layer``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Zeigen``
     - ``int32``
   * - ``Setzen``
     - ``int32``
   * - ``Lfdnr``
     - ``int32``
   * - ``Idreferenz``
     - ``string``
   * - ``ObjsString``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

No result properties found.

LFKT
^^^^
Object Type: ``LoadFactorTable``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Zeitoption``
     - ``int32``
   * - ``Intpol``
     - ``int32``
   * - ``Idreferenz``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``FWVB_DPHMIN``
   * - ``FWVB_TVLMIN``
   * - ``LF``
   * - ``MAINELEMENT``
   * - ``MFVHYUV``
   * - ``MFVTHUV``
   * - ``NFVHYUV``
   * - ``NFVTHUV``
   * - ``TVMINMAX``

LFKT_ROWT
^^^^^^^^^
Object Type: ``LoadFactorTable_Row``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Fk``
     - ``string``
   * - ``Zeit``
     - ``single``
   * - ``Zeitstempel``
     - ``string``
   * - ``Lf``
     - ``single``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

No result properties found.

RLVG
^^^^
Object Type: ``LogicalComparison``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Ka``
     - ``string``
   * - ``Indtyp``
     - ``int32``
   * - ``Fkcont``
     - ``string``
   * - ``E1``
     - ``string``
   * - ``E2``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``RglSymbolTyp``
     - ``rglsymboltype``
   * - ``SymbolFactor``
     - ``double``
   * - ``Angle``
     - ``double``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``bz.Fk``
     - ``string``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``MAINELEMENT``
   * - ``XA``
   * - ``XE1``
   * - ``XE2``

RLSR
^^^^
Object Type: ``LogicalStorage``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Ka``
     - ``string``
   * - ``Fkcont``
     - ``string``
   * - ``E1``
     - ``string``
   * - ``E2``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``RglSymbolTyp``
     - ``rglsymboltype``
   * - ``SymbolFactor``
     - ``double``
   * - ``Angle``
     - ``double``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``bz.Fk``
     - ``string``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``MAINELEMENT``
   * - ``XA``
   * - ``XE1``
   * - ``XE2``

SWVT
^^^^
Object Type: ``MeasuredVariableTable``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Zeitoption``
     - ``int32``
   * - ``Intpol``
     - ``int32``
   * - ``Idreferenz``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``MAINELEMENT``
   * - ``W``

SWVT_ROWT
^^^^^^^^^
Object Type: ``MeasuredVariableTable_Row``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Fk``
     - ``string``
   * - ``Zeit``
     - ``single``
   * - ``Zeitstempel``
     - ``string``
   * - ``W``
     - ``single``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

No result properties found.

RMMA
^^^^
Object Type: ``MinMaxSelection``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Ka``
     - ``string``
   * - ``Indmma``
     - ``int32``
   * - ``Fkcont``
     - ``string``
   * - ``E1``
     - ``string``
   * - ``E2``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``RglSymbolTyp``
     - ``rglsymboltype``
   * - ``SymbolFactor``
     - ``double``
   * - ``Angle``
     - ``double``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``bz.Fk``
     - ``string``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``MAINELEMENT``
   * - ``XA``
   * - ``XE1``
   * - ``XE2``

RMUL
^^^^
Object Type: ``Multiplier``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Ka``
     - ``string``
   * - ``Konst``
     - ``single``
   * - ``Indmul``
     - ``int32``
   * - ``Fkcont``
     - ``string``
   * - ``E1``
     - ``string``
   * - ``E2``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``RglSymbolTyp``
     - ``rglsymboltype``
   * - ``SymbolFactor``
     - ``double``
   * - ``Angle``
     - ``double``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``bz.Fk``
     - ``string``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``MAINELEMENT``
   * - ``MULT``
   * - ``XA``
   * - ``XE1``
   * - ``XE2``

NSCH
^^^^
Object Type: ``NetValve``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Typ``
     - ``int32``
   * - ``Poskm``
     - ``single``
   * - ``Fkrohr``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``SymbolFactor``
     - ``double``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.Indi``
     - ``int32``
   * - ``bz.Stellung``
     - ``int32``
   * - ``bz.Fkswvt``
     - ``string``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``MAINELEMENT``
   * - ``STELLUNG``

KNOT
^^^^
Object Type: ``Node``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Ktyp``
     - ``string``
   * - ``Zkor``
     - ``single``
   * - ``QmEin``
     - ``single``
   * - ``Lfakt``
     - ``single``
   * - ``Fkpzon``
     - ``string``
   * - ``Fkfstf``
     - ``string``
   * - ``Fkutmp``
     - ``string``
   * - ``Fkfqps``
     - ``string``
   * - ``Fkcont``
     - ``string``
   * - ``Fk2lknot``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``Iplanung``
     - ``int32``
   * - ``Kvr``
     - ``int32``
   * - ``Qakt``
     - ``double``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``NodeNamePosition``
     - ``int32``
   * - ``ShowNodeName``
     - ``boolean``
   * - ``KvrKlartext``
     - ``string``
   * - ``NumberOfVERB``
     - ``int32``
   * - ``HasBlockConnection``
     - ``boolean``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``SymbolFactor``
     - ``double``
   * - ``bz.Drakonz``
     - ``single``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.Fkpvar``
     - ``string``
   * - ``bz.Fkqvar``
     - ``string``
   * - ``bz.Fklfkt``
     - ``string``
   * - ``bz.PhEin``
     - ``single``
   * - ``bz.Tm``
     - ``single``
   * - ``bz.Te``
     - ``single``
   * - ``bz.PhMin``
     - ``single``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``BCIND``
   * - ``BCIND_CALC``
   * - ``BCIND_FLOW``
   * - ``BCIND_MODEL``
   * - ``BCIND_SOURCE``
   * - ``BCIND_TYPE``
   * - ``CHLORID``
   * - ``CP``
   * - ``DP``
   * - ``DPH``
   * - ``DYNVISKO``
   * - ``EH``
   * - ``EISENFILT``
   * - ``EISENGES``
   * - ``ESQUELLSP``
   * - ``FITT_ANGLE``
   * - ``FITT_BASTYPE``
   * - ``FITT_DP1``
   * - ``FITT_DP2``
   * - ``FITT_DP3``
   * - ``FITT_STATE``
   * - ``FITT_SUBTYPE``
   * - ``FITT_VBTYPE1``
   * - ``FITT_VBTYPE2``
   * - ``FITT_VBTYPE3``
   * - ``FITT_ZETA1``
   * - ``FITT_ZETA2``
   * - ``FITT_ZETA3``
   * - ``FSTF_NAME``
   * - ``GMIX_NAME``
   * - ``H``
   * - ``HI``
   * - ``HMAX_INST``
   * - ``HMIN_INST``
   * - ``HS``
   * - ``IAKTIV``
   * - ``INDUV``
   * - ``K``
   * - ``KP``
   * - ``KT``
   * - ``LEITFAEH``
   * - ``LFAKTAKT``
   * - ``LFKT``
   * - ``M``
   * - ``MAINELEMENT``
   * - ``MN``
   * - ``P``
   * - ``PDAMPF``
   * - ``PH``
   * - ``PH_EIN``
   * - ``PH_MIN``
   * - ``PHMINMAXDIF``
   * - ``PHWERT``
   * - ``PMAX_INST``
   * - ``PMIN_INST``
   * - ``PVAR``
   * - ``Q2``
   * - ``QM``
   * - ``QMABS``
   * - ``QVAR``
   * - ``RHO``
   * - ``RHON``
   * - ``RHONQUAL``
   * - ``SULFAT``
   * - ``T``
   * - ``TE``
   * - ``TEMP``
   * - ``TMAX_INST``
   * - ``TMIN_INST``
   * - ``TTR``
   * - ``VOLD``
   * - ``WALTER``
   * - ``ZHKNR``

PHIV
^^^^
Object Type: ``NonReturnValvesTable``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

No result properties found.

PHIV_ROWS
^^^^^^^^^
Object Type: ``NonReturnValvesTable_Row``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Fk``
     - ``string``
   * - ``V``
     - ``single``
   * - ``Phi``
     - ``single``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

No result properties found.

NRCV
^^^^
Object Type: ``NumericalDisplay``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Unit``
     - ``string``
   * - ``Decpoint``
     - ``int32``
   * - ``Abswert``
     - ``int32``
   * - ``Prftxt``
     - ``string``
   * - ``FkdpgrDpkt``
     - ``string``
   * - ``Fkcont``
     - ``string``
   * - ``Warncolor``
     - ``int32``
   * - ``Noticecolor``
     - ``int32``
   * - ``Alarmcolor``
     - ``int32``
   * - ``Thousandsep``
     - ``int32``
   * - ``Checkcolor``
     - ``int32``
   * - ``Beschreibung``
     - ``string``
   * - ``Indval``
     - ``int32``
   * - ``Objtype``
     - ``string``
   * - ``Attrtype``
     - ``string``
   * - ``Fkobjtype``
     - ``string``
   * - ``ResultValue``
     - ``string``
   * - ``PrefixWidth``
     - ``double``
   * - ``ElementFont``
     - ``c3sfont``
   * - ``ElementWarnColor``
     - ``color``
   * - ``ElementNoticeColor``
     - ``color``
   * - ``ElementAlarmColor``
     - ``color``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``BoundingRectangle``
     - ``irectangle``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``Angle``
     - ``double``
   * - ``bz.Fk``
     - ``string``

Result Properties
"""""""""""""""""

No result properties found.

CONT
^^^^
Object Type: ``ObjectContainerSymbol``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Id``
     - ``int32``
   * - ``Idparent``
     - ``int32``
   * - ``Lfdnr``
     - ``int32``
   * - ``Idreferenz``
     - ``string``
   * - ``SymbolType``
     - ``ccontsymboltype``
   * - ``SymbolFont``
     - ``c3sfont``
   * - ``PickingTolerance``
     - ``double``
   * - ``MaximalNodeWidth``
     - ``double``
   * - ``MaximalPipeWidth``
     - ``double``
   * - ``MaximalVbelNselWidth``
     - ``double``
   * - ``MeterPerPixel``
     - ``double``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``BoundingRectangle``
     - ``irectangle``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``bz.Fk``
     - ``string``

Result Properties
"""""""""""""""""

No result properties found.

OBEH
^^^^
Object Type: ``OpenContainer``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Indatab``
     - ``int32``
   * - ``A``
     - ``single``
   * - ``Hb``
     - ``single``
   * - ``Fkatab``
     - ``string``
   * - ``Dn``
     - ``single``
   * - ``Zetapos``
     - ``single``
   * - ``Zetaneg``
     - ``single``
   * - ``Knotk``
     - ``string``
   * - ``Zkor``
     - ``single``
   * - ``Fkfstf``
     - ``string``
   * - ``Fkknotfilling``
     - ``string``
   * - ``Filling``
     - ``int32``
   * - ``Fkcont``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``Iplanung``
     - ``int32``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``SymbolGraf``
     - ``symbol1c_graf``
   * - ``SymbolFactor``
     - ``double``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``Angle``
     - ``double``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.Wsp``
     - ``single``
   * - ``bz.Walter0``
     - ``single``
   * - ``bz.Tm0``
     - ``single``
   * - ``bz.WspNN``
     - ``double``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``DWST_DT``
   * - ``IAKTIV``
   * - ``M``
   * - ``MAINELEMENT``
   * - ``MEXT``
   * - ``QM``
   * - ``QMEXT``
   * - ``RHO``
   * - ``T``
   * - ``T0``
   * - ``V``
   * - ``VOL``
   * - ``WALTER``
   * - ``WALTER0``
   * - ``WST``
   * - ``WST0``

OVAL
^^^^
Object Type: ``Oval``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Fkcont``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``bz.Fk``
     - ``string``

Result Properties
"""""""""""""""""

No result properties found.

PARZ
^^^^
Object Type: ``PARZ_TransientCalculationParameters``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Jdampf``
     - ``int32``
   * - ``Thepdk``
     - ``single``
   * - ``Thepdr``
     - ``single``
   * - ``Jrst``
     - ``int32``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.Dt``
     - ``single``
   * - ``bz.Tmax``
     - ``single``
   * - ``bz.Dttrsp``
     - ``single``

Result Properties
"""""""""""""""""

No result properties found.

PHTR
^^^^
Object Type: ``PhaseSeparation``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Dn``
     - ``single``
   * - ``Zeta``
     - ``single``
   * - ``Fkcont``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``Iplanung``
     - ``int32``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``ShowDescription``
     - ``boolean``
   * - ``PositionOfDescription``
     - ``int32``
   * - ``Angle``
     - ``double``
   * - ``SymbolFactor``
     - ``double``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``bz.Fk``
     - ``string``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``DH``
   * - ``DP``
   * - ``IAKTIV``
   * - ``MAINELEMENT``
   * - ``MI``
   * - ``MK``
   * - ``Q``
   * - ``QM``
   * - ``RHOI``
   * - ``RHOK``
   * - ``V``

RPID
^^^^
Object Type: ``PidController``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Ka``
     - ``string``
   * - ``Kp``
     - ``single``
   * - ``Kd``
     - ``single``
   * - ``Td``
     - ``single``
   * - ``Xdzul``
     - ``single``
   * - ``Indein``
     - ``int32``
   * - ``Indint``
     - ``int32``
   * - ``Inddif``
     - ``int32``
   * - ``Wirk``
     - ``int32``
   * - ``Fkcont``
     - ``string``
   * - ``E1``
     - ``string``
   * - ``E2``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``RglSymbolTyp``
     - ``rglsymboltype``
   * - ``SymbolFactor``
     - ``double``
   * - ``Angle``
     - ``double``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``bz.Fk``
     - ``string``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``DYDT``
   * - ``DYDTD``
   * - ``DYDTI``
   * - ``DYDTP``
   * - ``MAINELEMENT``
   * - ``XA``
   * - ``XE1``
   * - ``XE2``

ROHR
^^^^
Object Type: ``Pipe``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``FkdtroRowd``
     - ``string``
   * - ``Fkltgr``
     - ``string``
   * - ``Fkstrasse``
     - ``string``
   * - ``L``
     - ``single``
   * - ``Lzu``
     - ``single``
   * - ``Rau``
     - ``single``
   * - ``Jlambs``
     - ``int32``
   * - ``Lambda0``
     - ``single``
   * - ``Zein``
     - ``single``
   * - ``Zaus``
     - ``single``
   * - ``Zuml``
     - ``single``
   * - ``Asoll``
     - ``single``
   * - ``Indschall``
     - ``int32``
   * - ``Baujahr``
     - ``string``
   * - ``Hal``
     - ``int32``
   * - ``Fkcont``
     - ``string``
   * - ``Fk2lrohr``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``Iplanung``
     - ``int32``
   * - ``Kvr``
     - ``int32``
   * - ``LineWidthMM``
     - ``double``
   * - ``DottedLine``
     - ``int32``
   * - ``DN``
     - ``string``
   * - ``Di``
     - ``single``
   * - ``KvrKlartext``
     - ``string``
   * - ``HasClosedNSCHs``
     - ``nullable`1``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.Qsvb``
     - ``single``
   * - ``bz.Irtrenn``
     - ``int32``
   * - ``bz.Leckstatus``
     - ``int32``
   * - ``bz.Leckstart``
     - ``single``
   * - ``bz.Leckend``
     - ``single``
   * - ``bz.Leckort``
     - ``single``
   * - ``bz.Leckmenge``
     - ``single``
   * - ``bz.Imptnz``
     - ``single``
   * - ``bz.Zvlimptnz``
     - ``double``
   * - ``bz.Kantenzv``
     - ``double``
   * - ``bz.ITrennWithNSCH``
     - ``int32``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``A``
   * - ``ACALC``
   * - ``CPI``
   * - ``CPK``
   * - ``DH``
   * - ``DP``
   * - ``DRAGRED``
   * - ``DRAKONZ``
   * - ``DSI``
   * - ``DSK``
   * - ``DTTR``
   * - ``DWVERL``
   * - ``DWVERLABS``
   * - ``ETAAV``
   * - ``FS``
   * - ``HR``
   * - ``HVEC``
   * - ``IAKTIV``
   * - ``IRTRENN``
   * - ``JV``
   * - ``JV2``
   * - ``LAMBDA``
   * - ``LECKEINAUS``
   * - ``LECKMENGE``
   * - ``LECKORT``
   * - ``LINEPACK``
   * - ``LINEPACKGEOM``
   * - ``LINEPACKRATE``
   * - ``MAINELEMENT``
   * - ``MAV``
   * - ``MI``
   * - ``MK``
   * - ``MKOND``
   * - ``MMAX_INST``
   * - ``MMIN_INST``
   * - ``MVEC``
   * - ``MVECMAX_INST``
   * - ``MVECMIN_INST``
   * - ``PAV``
   * - ``PDAMPF``
   * - ``PHR``
   * - ``PHVEC``
   * - ``PMAX``
   * - ``PMIN``
   * - ``PR``
   * - ``PVEC``
   * - ``PVECMAX_INST``
   * - ``PVECMIN_INST``
   * - ``QI2``
   * - ``QK2``
   * - ``QMAV``
   * - ``QMI``
   * - ``QMK``
   * - ``QMMAX_INST``
   * - ``QMMIN_INST``
   * - ``QMVEC``
   * - ``QSVB``
   * - ``RHOAV``
   * - ``RHOI``
   * - ``RHOK``
   * - ``RHOVEC``
   * - ``SVEC``
   * - ``TAV``
   * - ``TI``
   * - ``TK``
   * - ``TTRVEC``
   * - ``TVEC``
   * - ``TVECMAX_INST``
   * - ``TVECMIN_INST``
   * - ``VAV``
   * - ``VI``
   * - ``VK``
   * - ``VMAX_INST``
   * - ``VMIN_INST``
   * - ``VOLDA``
   * - ``WALTERI``
   * - ``WALTERK``
   * - ``WVL``
   * - ``ZAUS``
   * - ``ZEIN``
   * - ``ZHKNR``
   * - ``ZVEC``

LTGR
^^^^
Object Type: ``PipeGroup``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Verlegeart``
     - ``int32``
   * - ``Sichtbarkeit``
     - ``int32``
   * - ``Fksrat``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

No result properties found.

DTRO
^^^^
Object Type: ``PipeTable``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Typ``
     - ``string``
   * - ``E``
     - ``single``
   * - ``Idreferenz``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Zeitoption``
     - ``int32``

Result Properties
"""""""""""""""""

No result properties found.

DTRO_ROWD
^^^^^^^^^
Object Type: ``PipeTable_Row``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Fk``
     - ``string``
   * - ``Dn``
     - ``string``
   * - ``Di``
     - ``single``
   * - ``Da``
     - ``single``
   * - ``S``
     - ``single``
   * - ``Wsteig``
     - ``single``
   * - ``Wtiefe``
     - ``single``
   * - ``Kt``
     - ``single``
   * - ``Pn``
     - ``single``
   * - ``Ausfallzeit``
     - ``single``
   * - ``Reparatur``
     - ``single``
   * - ``Rehabilitation``
     - ``single``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

No result properties found.

ROHR_VRTX
^^^^^^^^^
Object Type: ``PipeVertex``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Fk``
     - ``string``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``Zkor``
     - ``single``
   * - ``Lfdnr``
     - ``int32``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``H``
   * - ``M``
   * - ``MAINELEMENT``
   * - ``MMAX_INST``
   * - ``MMIN_INST``
   * - ``P``
   * - ``PH``
   * - ``PMAX_INST``
   * - ``PMIN_INST``
   * - ``RHO``
   * - ``T``
   * - ``TMAX_INST``
   * - ``TMIN_INST``

PLYG
^^^^
Object Type: ``Polygon``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Fkcont``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``LineWidthMM``
     - ``double``
   * - ``LineColor``
     - ``color``
   * - ``FillColor``
     - ``color``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``bz.Fk``
     - ``string``

Result Properties
"""""""""""""""""

No result properties found.

POLY
^^^^
Object Type: ``Polyline``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Fkcont``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``LineWidthMM``
     - ``double``
   * - ``DottedLine``
     - ``int32``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``bz.Fk``
     - ``string``

Result Properties
"""""""""""""""""

No result properties found.

PREG
^^^^
Object Type: ``PressureRegulator``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Dn``
     - ``single``
   * - ``Typ``
     - ``int32``
   * - ``Indprg``
     - ``int32``
   * - ``Fkzep1``
     - ``string``
   * - ``Ts``
     - ``single``
   * - ``Fkcont``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``Iplanung``
     - ``int32``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``ShowDescription``
     - ``boolean``
   * - ``PositionOfDescription``
     - ``int32``
   * - ``Angle``
     - ``double``
   * - ``SymbolFactor``
     - ``double``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.Indsoll``
     - ``int32``
   * - ``bz.Phsoll``
     - ``single``
   * - ``bz.Fkswvt``
     - ``string``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``DH``
   * - ``DP``
   * - ``DPH``
   * - ``DSI``
   * - ``DSK``
   * - ``FS``
   * - ``HR``
   * - ``IAKTIV``
   * - ``KV``
   * - ``M``
   * - ``MAINELEMENT``
   * - ``PH``
   * - ``PHI``
   * - ``PHSOLL``
   * - ``PR``
   * - ``PSOLL``
   * - ``QM``
   * - ``RHO``
   * - ``SWVT``
   * - ``V``
   * - ``ZETA``

PZON
^^^^
Object Type: ``PressureZone``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Lfdnr``
     - ``int32``
   * - ``Modus``
     - ``int32``
   * - ``Idimra``
     - ``int32``
   * - ``Idimbh``
     - ``int32``
   * - ``Pkminra``
     - ``single``
   * - ``Pkmaxra``
     - ``single``
   * - ``Pkminbh``
     - ``single``
   * - ``Pkmaxbh``
     - ``single``
   * - ``Klpmin``
     - ``single``
   * - ``Idreferenz``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

No result properties found.

RPT1
^^^^
Object Type: ``Pt1Controller``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Ka``
     - ``string``
   * - ``Kp``
     - ``single``
   * - ``T1``
     - ``single``
   * - ``Fkcont``
     - ``string``
   * - ``E1``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``RglSymbolTyp``
     - ``rglsymboltype``
   * - ``SymbolFactor``
     - ``double``
   * - ``Angle``
     - ``double``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``bz.Fk``
     - ``string``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``MAINELEMENT``
   * - ``XA``
   * - ``XE``

PUMP
^^^^
Object Type: ``Pump``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Fkpumk``
     - ``string``
   * - ``Fkpumkturb``
     - ``string``
   * - ``Qmref``
     - ``single``
   * - ``Nref``
     - ``single``
   * - ``Href``
     - ``single``
   * - ``Pref``
     - ``single``
   * - ``Qmrefturb``
     - ``single``
   * - ``Nrefturb``
     - ``single``
   * - ``Hrefturb``
     - ``single``
   * - ``Prefturb``
     - ``single``
   * - ``Nmin``
     - ``single``
   * - ``Nmax``
     - ``single``
   * - ``Q0min``
     - ``single``
   * - ``Q0max``
     - ``single``
   * - ``Fkkref1``
     - ``string``
   * - ``Fkkref2``
     - ``string``
   * - ``Jwirk``
     - ``int32``
   * - ``Traeg``
     - ``single``
   * - ``Jrlsp``
     - ``int32``
   * - ``Dndtma``
     - ``single``
   * - ``Indl``
     - ``int32``
   * - ``Fketam``
     - ``string``
   * - ``Fketau``
     - ``string``
   * - ``Fketar``
     - ``string``
   * - ``Nemot``
     - ``single``
   * - ``Etamot``
     - ``single``
   * - ``Schlupf``
     - ``single``
   * - ``Bkfak``
     - ``single``
   * - ``Tsig``
     - ``single``
   * - ``Dndt``
     - ``single``
   * - ``Ntrudel``
     - ``single``
   * - ``Dngross``
     - ``single``
   * - ``Dnklein``
     - ``single``
   * - ``Dt0aus``
     - ``single``
   * - ``Indasf``
     - ``int32``
   * - ``Wscasf``
     - ``single``
   * - ``Fkkiasf``
     - ``string``
   * - ``Totasf``
     - ``single``
   * - ``Wirasf``
     - ``int32``
   * - ``Indaps``
     - ``int32``
   * - ``Psa``
     - ``single``
   * - ``Fkkiaps``
     - ``string``
   * - ``Totaps``
     - ``single``
   * - ``Indapd``
     - ``int32``
   * - ``Papd``
     - ``single``
   * - ``Fkkiapd``
     - ``string``
   * - ``Totapd``
     - ``single``
   * - ``Fkcont``
     - ``string``
   * - ``Dt0sch``
     - ``single``
   * - ``Indds``
     - ``int32``
   * - ``Pdsein``
     - ``single``
   * - ``Fkkrsspd``
     - ``string``
   * - ``Kpds``
     - ``single``
   * - ``Kids``
     - ``single``
   * - ``Kdds``
     - ``single``
   * - ``Indss``
     - ``int32``
   * - ``Pssein``
     - ``single``
   * - ``Fkkrssps``
     - ``string``
   * - ``Kpss``
     - ``single``
   * - ``Kiss``
     - ``single``
   * - ``Kdss``
     - ``single``
   * - ``Indstf``
     - ``int32``
   * - ``Wscstf``
     - ``single``
   * - ``Fkkr1stf``
     - ``string``
   * - ``Wirstf``
     - ``int32``
   * - ``Kpstf``
     - ``single``
   * - ``Kistf``
     - ``single``
   * - ``Kdstf``
     - ``single``
   * - ``Indstd``
     - ``int32``
   * - ``Ifgsw``
     - ``int32``
   * - ``Wsostd``
     - ``single``
   * - ``Fkkr3std``
     - ``string``
   * - ``Fkkr4std``
     - ``string``
   * - ``Wirstd``
     - ``int32``
   * - ``Kpstd``
     - ``single``
   * - ``Kistd``
     - ``single``
   * - ``Kdstd``
     - ``single``
   * - ``Dt0std``
     - ``single``
   * - ``Idreferenz``
     - ``string``
   * - ``Iplanung``
     - ``int32``
   * - ``PerformanceMapParameters``
     - ``ipukennparams``
   * - ``BKFaktTubine``
     - ``single``
   * - ``EtaRef``
     - ``nullable`1``
   * - ``EtaRefTurb``
     - ``nullable`1``
   * - ``IndLTurb``
     - ``int32``
   * - ``NMaxTurb``
     - ``single``
   * - ``NMinTurb``
     - ``single``
   * - ``Q0MaxTurb``
     - ``single``
   * - ``Q0MinTurb``
     - ``single``
   * - ``PukfString``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``ShowDescription``
     - ``boolean``
   * - ``PositionOfDescription``
     - ``int32``
   * - ``Angle``
     - ``double``
   * - ``SymbolFactor``
     - ``double``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.Inds``
     - ``int32``
   * - ``bz.Indturb``
     - ``int32``
   * - ``bz.Ispu``
     - ``int32``
   * - ``bz.Isputurb``
     - ``int32``
   * - ``bz.Qmsoll``
     - ``single``
   * - ``bz.Nsoll``
     - ``single``
   * - ``bz.Qmsollturb``
     - ``single``
   * - ``bz.Nsollturb``
     - ``single``
   * - ``bz.Phsoll``
     - ``single``
   * - ``bz.Fkrcpl``
     - ``string``
   * - ``bz.Inda``
     - ``int32``
   * - ``bz.Tipu``
     - ``single``
   * - ``bz.Fkpumd``
     - ``string``
   * - ``bz.Fkswvt``
     - ``string``
   * - ``bz.IndATurb``
     - ``int32``
   * - ``bz.IndSTurb``
     - ``int32``
   * - ``bz.IndsKlartext``
     - ``string``
   * - ``bz.IndaKlartext``
     - ``string``
   * - ``bz.IspuKlartext``
     - ``string``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``BK``
   * - ``DH``
   * - ``DP``
   * - ``DPH``
   * - ``EINAUS``
   * - ``ETA``
   * - ``ETAW``
   * - ``IAKTIV``
   * - ``IND``
   * - ``M``
   * - ``MAINELEMENT``
   * - ``MOM``
   * - ``N``
   * - ``NMINMAXDIF``
   * - ``NPSH``
   * - ``NPSHDIF``
   * - ``NPSHMIN``
   * - ``NSOLLTURB``
   * - ``PA``
   * - ``PE``
   * - ``PE_RUECK``
   * - ``PHSOLL``
   * - ``PP``
   * - ``PUMD``
   * - ``QM``
   * - ``QMSOLL``
   * - ``QMSOLLTURB``
   * - ``QN0``
   * - ``RCPU_IND``
   * - ``RCPU_W``
   * - ``RCPU_X``
   * - ``RCPU_XD``
   * - ``RHO``
   * - ``STOERUNG``
   * - ``SWVT``

PUMK
^^^^
Object Type: ``PumpCharTable``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``N``
     - ``single``
   * - ``Typ``
     - ``int32``
   * - ``Rhobzg``
     - ``single``
   * - ``Beschreibung``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Zeitoption``
     - ``int32``

Result Properties
"""""""""""""""""

No result properties found.

PUMK_ROWS
^^^^^^^^^
Object Type: ``PumpCharTable_Row``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Fk``
     - ``string``
   * - ``Q``
     - ``single``
   * - ``H``
     - ``single``
   * - ``P``
     - ``single``
   * - ``Eta``
     - ``single``
   * - ``Npsh``
     - ``single``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

No result properties found.

PGRP
^^^^
Object Type: ``PumpGroup``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Ibyp``
     - ``int32``
   * - ``ActAsa``
     - ``int32``
   * - ``AusAsa``
     - ``int32``
   * - ``Fkkibyp``
     - ``string``
   * - ``Fkkkbyp``
     - ``string``
   * - ``Ischalt``
     - ``int32``
   * - ``Qmaus``
     - ``single``
   * - ``Dphaus``
     - ``single``
   * - ``Indrst``
     - ``int32``
   * - ``Nmax``
     - ``single``
   * - ``Pdmax``
     - ``single``
   * - ``Fkkdmax``
     - ``string``
   * - ``Psmin``
     - ``single``
   * - ``Fkksmin``
     - ``string``
   * - ``Fkcont``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``Iplanung``
     - ``int32``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``BoundingRectangle``
     - ``irectangle``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.Iaktiv``
     - ``int32``
   * - ``bz.Indpg``
     - ``int32``
   * - ``bz.Fkrart``
     - ``string``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``BK``
   * - ``DH``
   * - ``DP``
   * - ``DPH``
   * - ``ETA``
   * - ``IAKTIV``
   * - ``INDPG``
   * - ``INDSTD``
   * - ``IZSTPG``
   * - ``M``
   * - ``MAINELEMENT``
   * - ``NPUMPIST``
   * - ``NPUMPSOLL``
   * - ``PE``
   * - ``QM``
   * - ``RART``
   * - ``RHO``
   * - ``W``
   * - ``X``

PGRP_PUMP
^^^^^^^^^
Object Type: ``PumpOfPumpGroup``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Fkpgrp``
     - ``string``
   * - ``Fkpump``
     - ``string``
   * - ``Lfdnr``
     - ``int32``
   * - ``Iplanung``
     - ``int32``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.Iaktiv``
     - ``int32``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``IAKTIV``
   * - ``MAINELEMENT``

PUMD
^^^^
Object Type: ``PumpSpeedTable``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Zeitoption``
     - ``int32``
   * - ``Intpol``
     - ``int32``
   * - ``Idreferenz``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``MAINELEMENT``
   * - ``N``

PUMD_ROWT
^^^^^^^^^
Object Type: ``PumpSpeedTable_Row``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Fk``
     - ``string``
   * - ``Zeit``
     - ``single``
   * - ``Zeitstempel``
     - ``string``
   * - ``N``
     - ``single``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

No result properties found.

ERROR_NO_MAPPING__RART_ControlMode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Object Type: ``RART_ControlMode``


Properties
""""""""""

No properties found.

Result Properties
"""""""""""""""""

No result properties found.

REGP
^^^^
Object Type: ``REGP_ControlParameters``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Dt0reg``
     - ``single``
   * - ``Indreg``
     - ``int32``
   * - ``FlagsUser``
     - ``int32``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

No result properties found.

RMES_DPTS
^^^^^^^^^
Object Type: ``RMES_DPTS_RmesInternalDataPoint``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Fkrmes``
     - ``string``
   * - ``Lfdnr``
     - ``int32``
   * - ``Indfunc``
     - ``int32``
   * - ``Factor``
     - ``single``
   * - ``Addend``
     - ``single``
   * - ``ObjectTypeDescription``
     - ``string``
   * - ``AttributeDescription``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.Objtype``
     - ``string``
   * - ``bz.Attrtype``
     - ``string``
   * - ``bz.Fkobjtype``
     - ``string``

Result Properties
"""""""""""""""""

No result properties found.

RECT
^^^^
Object Type: ``Rectangle``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Fkcont``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``LineWidthMM``
     - ``double``
   * - ``LineColor``
     - ``color``
   * - ``FillColor``
     - ``color``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``bz.Fk``
     - ``string``

Result Properties
"""""""""""""""""

No result properties found.

ZEP1
^^^^
Object Type: ``RegulatorsTable``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Typ``
     - ``int32``
   * - ``Kvbzg``
     - ``single``
   * - ``Beschreibung``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Zeitoption``
     - ``int32``

Result Properties
"""""""""""""""""

No result properties found.

ZEP1_ROWS
^^^^^^^^^
Object Type: ``RegulatorsTable_Row``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Fk``
     - ``string``
   * - ``Phi``
     - ``single``
   * - ``Zeta``
     - ``single``
   * - ``Kvrel``
     - ``single``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

No result properties found.

TRFT
^^^^
Object Type: ``ReturnTemperaturTable``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Zeitoption``
     - ``int32``

Result Properties
"""""""""""""""""

No result properties found.

TRFT_ROWS
^^^^^^^^^
Object Type: ``ReturnTemperaturTable_Row``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Fk``
     - ``string``
   * - ``Lfth``
     - ``single``
   * - ``Trs``
     - ``single``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

No result properties found.

RRCT
^^^^
Object Type: ``RoundRectangle``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Fkcont``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``LineWidthMM``
     - ``double``
   * - ``LineColor``
     - ``color``
   * - ``FillColor``
     - ``color``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``bz.Fk``
     - ``string``

Result Properties
"""""""""""""""""

No result properties found.

ERROR_NO_MAPPING__SIRGRAF
^^^^^^^^^^^^^^^^^^^^^^^^^
Object Type: ``SIRGRAF``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Nknr``
     - ``int32``
   * - ``Nbnr``
     - ``int32``
   * - ``Sylw``
     - ``single``
   * - ``Upkc``
     - ``int32``
   * - ``Scelt``
     - ``int32``
   * - ``Sccnln``
     - ``int32``
   * - ``Scknot``
     - ``int32``
   * - ``Scrohr``
     - ``int32``
   * - ``Sfvbels``
     - ``double``
   * - ``Tooltip``
     - ``int32``
   * - ``HighlightElement``
     - ``int32``
   * - ``Uimode``
     - ``int32``
   * - ``Pickingmode``
     - ``int32``
   * - ``LegFix``
     - ``int32``
   * - ``LegXkor``
     - ``double``
   * - ``LegYkor``
     - ``double``
   * - ``LegHeight``
     - ``single``
   * - ``LegMaxEntries``
     - ``int32``
   * - ``PickingRadius``
     - ``int32``
   * - ``MaxNodeSize``
     - ``int32``
   * - ``MaxLineSize``
     - ``int32``
   * - ``MaxVbelSize``
     - ``int32``
   * - ``BlockBkgndColor``
     - ``int32``
   * - ``TileDownloadServer``
     - ``string``
   * - ``OsmUser``
     - ``string``
   * - ``OsmPasswd``
     - ``string``
   * - ``UseHttpProxy``
     - ``int32``
   * - ``ProxyServer``
     - ``string``
   * - ``ProxyUser``
     - ``string``
   * - ``ProxyPasswd``
     - ``string``
   * - ``ProxyAuthMethod``
     - ``int32``
   * - ``CacheInUserProfile``
     - ``int32``
   * - ``CacheDirectory``
     - ``string``
   * - ``ImageQuality``
     - ``int32``
   * - ``Srid``
     - ``int32``
   * - ``Srid2``
     - ``int32``
   * - ``DrawTileOutlines``
     - ``int32``
   * - ``OsmTimeout``
     - ``int32``
   * - ``ListConfigString``
     - ``string``
   * - ``StructuredViewsString``
     - ``string``
   * - ``SridString``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

No result properties found.

SPLZ
^^^^
Object Type: ``SPLZ_TimeSeries``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Lfdnr``
     - ``int32``
   * - ``Aktiv``
     - ``int32``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

No result properties found.

SIVE
^^^^
Object Type: ``SafetyValve``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Dn``
     - ``single``
   * - ``Typ``
     - ``int32``
   * - ``Fkkref``
     - ``string``
   * - ``Fkzep2``
     - ``string``
   * - ``Fkphi2``
     - ``string``
   * - ``Fkcont``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``Iplanung``
     - ``int32``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``ShowDescription``
     - ``boolean``
   * - ``PositionOfDescription``
     - ``int32``
   * - ``Angle``
     - ``double``
   * - ``SymbolFactor``
     - ``double``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.Phis``
     - ``single``
   * - ``bz.Psch``
     - ``single``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``DH``
   * - ``DP``
   * - ``DPH``
   * - ``DSI``
   * - ``DSK``
   * - ``FS``
   * - ``HR``
   * - ``IAKTIV``
   * - ``M``
   * - ``MAINELEMENT``
   * - ``PHI``
   * - ``PHSCH``
   * - ``PR``
   * - ``QM``
   * - ``RHO``
   * - ``V``
   * - ``ZETA``

RSLW
^^^^
Object Type: ``SetpointDevice``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Ka``
     - ``string``
   * - ``Wmin``
     - ``single``
   * - ``Wmax``
     - ``single``
   * - ``Indwbg``
     - ``int32``
   * - ``Indwno``
     - ``int32``
   * - ``Fkcont``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``RglSymbolTyp``
     - ``rglsymboltype``
   * - ``SymbolFactor``
     - ``double``
   * - ``Angle``
     - ``double``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.Indslw``
     - ``int32``
   * - ``bz.Slwkon``
     - ``single``
   * - ``bz.Fkswvt``
     - ``string``
   * - ``bz.Fklfkt``
     - ``string``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``LFKT``
   * - ``MAINELEMENT``
   * - ``SLWKON``
   * - ``SWVT``
   * - ``W``
   * - ``WAKT``
   * - ``WE``
   * - ``WEAKT``
   * - ``WERCK``
   * - ``WRCK``
   * - ``XA``

SOKO
^^^^
Object Type: ``SolarCollector``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Typ``
     - ``int32``
   * - ``Bruttfl``
     - ``single``
   * - ``Apertfl``
     - ``single``
   * - ``Indfl``
     - ``int32``
   * - ``Eta0hem``
     - ``single``
   * - ``A1``
     - ``single``
   * - ``A2``
     - ``single``
   * - ``Eta0b``
     - ``single``
   * - ``C1``
     - ``single``
   * - ``C2``
     - ``single``
   * - ``C3``
     - ``single``
   * - ``Kthetad``
     - ``single``
   * - ``Ceff``
     - ``single``
   * - ``Indiam``
     - ``int32``
   * - ``Iamew00``
     - ``single``
   * - ``Iamew10``
     - ``single``
   * - ``Iamew20``
     - ``single``
   * - ``Iamew30``
     - ``single``
   * - ``Iamew40``
     - ``single``
   * - ``Iamew50``
     - ``single``
   * - ``Iamew60``
     - ``single``
   * - ``Iamew70``
     - ``single``
   * - ``Iamew80``
     - ``single``
   * - ``Iamew90``
     - ``single``
   * - ``Iamns00``
     - ``single``
   * - ``Iamns10``
     - ``single``
   * - ``Iamns20``
     - ``single``
   * - ``Iamns30``
     - ``single``
   * - ``Iamns40``
     - ``single``
   * - ``Iamns50``
     - ``single``
   * - ``Iamns60``
     - ``single``
   * - ``Iamns70``
     - ``single``
   * - ``Iamns80``
     - ``single``
   * - ``Iamns90``
     - ``single``
   * - ``Idreferenz``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

No result properties found.

STRO
^^^^
Object Type: ``StandPipe``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Indatab``
     - ``int32``
   * - ``A``
     - ``single``
   * - ``Hb``
     - ``single``
   * - ``U``
     - ``single``
   * - ``Mue``
     - ``single``
   * - ``Fkatab``
     - ``string``
   * - ``Dn``
     - ``single``
   * - ``Zetapos``
     - ``single``
   * - ``Zetaneg``
     - ``single``
   * - ``Knotk``
     - ``string``
   * - ``Zkor``
     - ``single``
   * - ``Fkfstf``
     - ``string``
   * - ``Fkcont``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``Iplanung``
     - ``int32``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``SymbolGraf``
     - ``symbol1c_graf``
   * - ``SymbolFactor``
     - ``double``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``Angle``
     - ``double``
   * - ``bz.Fk``
     - ``string``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``IAKTIV``
   * - ``M``
   * - ``MAINELEMENT``
   * - ``MUEB``
   * - ``QM``
   * - ``QMUEB``
   * - ``RHO``
   * - ``T``
   * - ``V``
   * - ``VOL``
   * - ``WALTER``
   * - ``WST``

STRASSE
^^^^^^^
Object Type: ``Street``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Nummer``
     - ``string``
   * - ``Ort``
     - ``string``
   * - ``Ortsteil``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``GeometriesDiffer``
     - ``boolean``

Result Properties
"""""""""""""""""

No result properties found.

RADD
^^^^
Object Type: ``SummingPoint``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Ka``
     - ``string``
   * - ``Indadd``
     - ``int32``
   * - ``Fkcont``
     - ``string``
   * - ``E1``
     - ``string``
   * - ``E2``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``RglSymbolTyp``
     - ``rglsymboltype``
   * - ``SymbolFactor``
     - ``double``
   * - ``Angle``
     - ``double``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``bz.Fk``
     - ``string``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``MAINELEMENT``
   * - ``XA``
   * - ``XE1``
   * - ``XE2``

BREF
^^^^
Object Type: ``SwitchInBlock``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Fkblock``
     - ``string``
   * - ``Fkcont``
     - ``string``
   * - ``TextColor``
     - ``color``
   * - ``ElementFont``
     - ``c3sfont``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``BoundingRectangle``
     - ``irectangle``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``

Result Properties
"""""""""""""""""

No result properties found.

TEVT
^^^^
Object Type: ``TemperatureTable``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Zeitoption``
     - ``int32``
   * - ``Intpol``
     - ``int32``
   * - ``Idreferenz``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``MAINELEMENT``
   * - ``T``

TEVT_ROWT
^^^^^^^^^
Object Type: ``TemperatureTable_Row``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Fk``
     - ``string``
   * - ``Zeit``
     - ``single``
   * - ``Zeitstempel``
     - ``string``
   * - ``T``
     - ``single``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

No result properties found.

GTXT
^^^^
Object Type: ``Text``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Fkcont``
     - ``string``
   * - ``Graftext``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``ElementColor``
     - ``color``
   * - ``ElementFont``
     - ``c3sfont``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``Angle``
     - ``double``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``bz.Fk``
     - ``string``

Result Properties
"""""""""""""""""

No result properties found.

WEVT
^^^^
Object Type: ``ThermalOutputTable``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Zeitoption``
     - ``int32``
   * - ``Intpol``
     - ``int32``
   * - ``Idreferenz``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``MAINELEMENT``
   * - ``W``

WEVT_ROWT
^^^^^^^^^
Object Type: ``ThermalOutputTable_Row``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Fk``
     - ``string``
   * - ``Zeit``
     - ``single``
   * - ``Zeitstempel``
     - ``string``
   * - ``W``
     - ``single``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

No result properties found.

STOF
^^^^
Object Type: ``ThermophysPropTable``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Zeitoption``
     - ``int32``

Result Properties
"""""""""""""""""

No result properties found.

STOF_ROWS
^^^^^^^^^
Object Type: ``ThermophysPropTable_Row``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Fk``
     - ``string``
   * - ``T``
     - ``single``
   * - ``Rho``
     - ``single``
   * - ``Nue``
     - ``single``
   * - ``Pd``
     - ``single``
   * - ``Cp``
     - ``single``
   * - ``Lambda``
     - ``single``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

No result properties found.

RUES
^^^^
Object Type: ``TransitionSymbol``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Iotyp``
     - ``int32``
   * - ``Idue``
     - ``string``
   * - ``Fkcont``
     - ``string``
   * - ``InputRues``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Ka``
     - ``string``
   * - ``RglSymbolTyp``
     - ``rglsymboltype``
   * - ``SymbolFactor``
     - ``double``
   * - ``Angle``
     - ``double``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``bz.Fk``
     - ``string``

Result Properties
"""""""""""""""""

No result properties found.

RMES
^^^^
Object Type: ``Transmitter``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Ka``
     - ``string``
   * - ``Mesdt0``
     - ``single``
   * - ``Indaggreg``
     - ``int32``
   * - ``Xumm``
     - ``single``
   * - ``Xumb``
     - ``single``
   * - ``Indxum``
     - ``int32``
   * - ``Xmin``
     - ``single``
   * - ``Xmax``
     - ``single``
   * - ``Indxbg``
     - ``int32``
   * - ``Indxno``
     - ``int32``
   * - ``Fkcont``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``RglSymbolTyp``
     - ``rglsymboltype``
   * - ``SymbolFactor``
     - ``double``
   * - ``Angle``
     - ``double``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.X0``
     - ``single``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``MAINELEMENT``
   * - ``XA``
   * - ``XM``
   * - ``XU``

TRVA
^^^^
Object Type: ``TransportVariable``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Jqualpar``
     - ``int32``
   * - ``Jtrsptyp``
     - ``int32``
   * - ``Jwalter``
     - ``int32``
   * - ``Jtemp``
     - ``int32``
   * - ``Jeisenges``
     - ``int32``
   * - ``Jeisenfilt``
     - ``int32``
   * - ``Jsulfat``
     - ``int32``
   * - ``Jchlorid``
     - ``int32``
   * - ``Jleitfaeh``
     - ``int32``
   * - ``Jphwert``
     - ``int32``
   * - ``Jhs``
     - ``int32``
   * - ``Jhi``
     - ``int32``
   * - ``Jrhon``
     - ``int32``
   * - ``Jmn``
     - ``int32``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

No result properties found.

USCH
^^^^
Object Type: ``USCH_UserDefinedProperties``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Objtype``
     - ``string``
   * - ``Valtype``
     - ``int32``
   * - ``Description``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

No result properties found.

ERROR_NO_MAPPING__Unknown
^^^^^^^^^^^^^^^^^^^^^^^^^
Object Type: ``Unknown``


Properties
""""""""""

No properties found.

Result Properties
"""""""""""""""""

No result properties found.

VARA
^^^^
Object Type: ``VARA_ColorScale``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Showarrow``
     - ``int32``
   * - ``Lfdnr``
     - ``int32``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

No result properties found.

VARA_ROWS
^^^^^^^^^
Object Type: ``VARA_ROWS_WidthOrScale``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Fk``
     - ``string``
   * - ``Cwtype``
     - ``int32``
   * - ``Reseletype``
     - ``string``
   * - ``Attype``
     - ``string``
   * - ``Prop``
     - ``string``
   * - ``Proptype``
     - ``int32``
   * - ``Valuestart``
     - ``single``
   * - ``Valueend``
     - ``single``
   * - ``Valuelb``
     - ``single``
   * - ``Valueub``
     - ``single``
   * - ``Valueconst``
     - ``single``
   * - ``Cwstart``
     - ``single``
   * - ``Cwend``
     - ``single``
   * - ``Colormid``
     - ``int32``
   * - ``Cwmode``
     - ``int32``
   * - ``Numcolor``
     - ``int32``
   * - ``Csvpfad``
     - ``string``
   * - ``Icsvidprop``
     - ``string``
   * - ``Icsvcolid``
     - ``int32``
   * - ``Icsvcolval``
     - ``int32``
   * - ``Iinvert``
     - ``int32``
   * - ``Iabsvalue``
     - ``int32``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

No result properties found.

VRCT
^^^^
Object Type: ``VRCT_ViewRectangle``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``XLinks``
     - ``single``
   * - ``YOben``
     - ``single``
   * - ``XRechts``
     - ``single``
   * - ``YUnten``
     - ``single``
   * - ``Lfdnr``
     - ``int32``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

No result properties found.

VENT
^^^^
Object Type: ``Valve``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Dn``
     - ``single``
   * - ``Typ``
     - ``int32``
   * - ``Indzeta``
     - ``int32``
   * - ``Zetapos``
     - ``single``
   * - ``Zetaneg``
     - ``single``
   * - ``Zetag``
     - ``single``
   * - ``Fkzep2``
     - ``string``
   * - ``Tsig``
     - ``single``
   * - ``Thub``
     - ``single``
   * - ``Indhub``
     - ``int32``
   * - ``Thub1``
     - ``single``
   * - ``Thub2``
     - ``single``
   * - ``Tpaus``
     - ``single``
   * - ``Fkcont``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``Iplanung``
     - ``int32``
   * - ``TypKlartext``
     - ``string``
   * - ``IndzetaKlartext``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``ShowDescription``
     - ``boolean``
   * - ``PositionOfDescription``
     - ``int32``
   * - ``Angle``
     - ``double``
   * - ``SymbolFactor``
     - ``double``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.Indphi``
     - ``int32``
   * - ``bz.Phio``
     - ``single``
   * - ``bz.Phig``
     - ``single``
   * - ``bz.Phisoll``
     - ``single``
   * - ``bz.Fkphi1``
     - ``string``
   * - ``bz.Tiv``
     - ``single``
   * - ``bz.IndPhiKonst``
     - ``int32``
   * - ``bz.IndphiKlartext``
     - ``string``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``AUF``
   * - ``AUFZU``
   * - ``DH``
   * - ``DP``
   * - ``DSI``
   * - ``DSK``
   * - ``FREIGABE``
   * - ``FS``
   * - ``HR``
   * - ``IAKTIV``
   * - ``KV``
   * - ``LAEUFT``
   * - ``M``
   * - ``MAINELEMENT``
   * - ``OEFFNET``
   * - ``PHI``
   * - ``PHI1``
   * - ``PHR``
   * - ``PR``
   * - ``Q2``
   * - ``QM``
   * - ``RHO``
   * - ``SCHLIESST``
   * - ``STOERUNG``
   * - ``V``
   * - ``ZETA``
   * - ``ZU``

PHI1
^^^^
Object Type: ``ValveLiftTable``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Zeitoption``
     - ``int32``
   * - ``Intpol``
     - ``int32``
   * - ``Idreferenz``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``MAINELEMENT``
   * - ``PHI``

PHI1_ROWT
^^^^^^^^^
Object Type: ``ValveLiftTable_Row``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Fk``
     - ``string``
   * - ``Zeit``
     - ``single``
   * - ``Zeitstempel``
     - ``string``
   * - ``Phi``
     - ``single``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

No result properties found.

QVAR
^^^^
Object Type: ``VarFlowTable``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Zeitoption``
     - ``int32``
   * - ``Intpol``
     - ``int32``
   * - ``Idreferenz``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``FWVB_DPHMIN``
   * - ``FWVB_TVLMIN``
   * - ``MAINELEMENT``
   * - ``MFVHYUV``
   * - ``MFVTHUV``
   * - ``NFVHYUV``
   * - ``NFVTHUV``
   * - ``QM``
   * - ``TVMINMAX``

QVAR_ROWT
^^^^^^^^^
Object Type: ``VarFlowTable_Row``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Fk``
     - ``string``
   * - ``Zeit``
     - ``single``
   * - ``Zeitstempel``
     - ``string``
   * - ``Qm``
     - ``single``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

No result properties found.

PVAR
^^^^
Object Type: ``VarPressureTable``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Zeitoption``
     - ``int32``
   * - ``Intpol``
     - ``int32``
   * - ``Idreferenz``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``MAINELEMENT``
   * - ``PH``

PVAR_ROWT
^^^^^^^^^
Object Type: ``VarPressureTable_Row``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Fk``
     - ``string``
   * - ``Zeit``
     - ``single``
   * - ``Zeitstempel``
     - ``string``
   * - ``Ph``
     - ``single``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

No result properties found.

PHI2
^^^^
Object Type: ``VentOpenCloseTable``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Zeitoption``
     - ``int32``

Result Properties
"""""""""""""""""

No result properties found.

PHI2_ROWS
^^^^^^^^^
Object Type: ``VentOpenCloseTable_Row``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Fk``
     - ``string``
   * - ``Zeit``
     - ``single``
   * - ``Phio``
     - ``single``
   * - ``Phis``
     - ``single``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

No result properties found.

BEVE
^^^^
Object Type: ``VentValve``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Dgr``
     - ``single``
   * - ``Dkl``
     - ``single``
   * - ``Alpha``
     - ``single``
   * - ``Vgrest``
     - ``single``
   * - ``Qlbmax``
     - ``single``
   * - ``Qlekl``
     - ``single``
   * - ``Rgbeve``
     - ``single``
   * - ``Trohr``
     - ``single``
   * - ``Poeff``
     - ``single``
   * - ``Ibedef``
     - ``int32``
   * - ``Ibetyp``
     - ``int32``
   * - ``Knotk``
     - ``string``
   * - ``Zkor``
     - ``single``
   * - ``Fkfstf``
     - ``string``
   * - ``Iekl``
     - ``int32``
   * - ``Fkcont``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``Iplanung``
     - ``int32``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``SymbolGraf``
     - ``symbol1c_graf``
   * - ``SymbolFactor``
     - ``double``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``Angle``
     - ``double``
   * - ``bz.Fk``
     - ``string``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``IAKTIV``
   * - ``IND``
   * - ``M``
   * - ``MAINELEMENT``
   * - ``MLUFT``
   * - ``PHI``
   * - ``PLUFT``
   * - ``QLUFT``
   * - ``QM``
   * - ``QMLUFT``
   * - ``RHO``
   * - ``TLUFT``
   * - ``VLUFT``
   * - ``VOLLUFT``

BEWI
^^^^
Object Type: ``VentilatedPressureAirVessel``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Indatab``
     - ``int32``
   * - ``A``
     - ``single``
   * - ``Lta``
     - ``single``
   * - ``Hb``
     - ``single``
   * - ``Pg0``
     - ``single``
   * - ``Tgas``
     - ``single``
   * - ``Fkatab``
     - ``string``
   * - ``Dn``
     - ``single``
   * - ``Zetapos``
     - ``single``
   * - ``Zetaneg``
     - ``single``
   * - ``Rgas``
     - ``single``
   * - ``Rpoly``
     - ``single``
   * - ``Knotk``
     - ``string``
   * - ``Zkor``
     - ``single``
   * - ``Fkfstf``
     - ``string``
   * - ``Fkcont``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``Iplanung``
     - ``int32``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``SymbolGraf``
     - ``symbol1c_graf``
   * - ``SymbolFactor``
     - ``double``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``Angle``
     - ``double``
   * - ``bz.Fk``
     - ``string``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``HLUFT``
   * - ``IAKTIV``
   * - ``IND``
   * - ``M``
   * - ``MAINELEMENT``
   * - ``PLUFT``
   * - ``QM``
   * - ``RHO``
   * - ``T``
   * - ``TLUFT``
   * - ``V``
   * - ``VOL``
   * - ``VOLLUFT``
   * - ``VOLLUFT1``
   * - ``WALTER``
   * - ``WST``

WBLZ
^^^^
Object Type: ``WBLZ_ThermalBalance``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Typ``
     - ``string``
   * - ``Aktiv``
     - ``int32``
   * - ``Idim``
     - ``int32``
   * - ``Idreferenz``
     - ``string``
   * - ``ObjsString``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``MAINELEMENT``
   * - ``WES``
   * - ``WRAND``
   * - ``WSPEI``
   * - ``WSPEI_SP``
   * - ``WVB``
   * - ``WVB_0``
   * - ``WVB_W``
   * - ``WVB_XD``
   * - ``WVERL``
   * - ``WWU``

WTTR
^^^^
Object Type: ``WeatherDataTable``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``Stdlon``
     - ``single``
   * - ``Lon``
     - ``single``
   * - ``Lat``
     - ``single``
   * - ``Albedo``
     - ``single``
   * - ``Zeitoption``
     - ``int32``
   * - ``Intpol``
     - ``int32``
   * - ``Idreferenz``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``GDIFF``
   * - ``GGLOB``
   * - ``MAINELEMENT``
   * - ``TEMP``
   * - ``WIND``

WTTR_ROWT
^^^^^^^^^
Object Type: ``WeatherDataTable_Row``


Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ``string``
   * - ``Fk``
     - ``string``
   * - ``Zeit``
     - ``single``
   * - ``Zeitstempel``
     - ``string``
   * - ``Temp``
     - ``single``
   * - ``Wind``
     - ``single``
   * - ``Gglob``
     - ``single``
   * - ``Gdiff``
     - ``single``
   * - ``Pk``
     - ``string``
   * - ``InVariant``
     - ``boolean``

Result Properties
"""""""""""""""""

No result properties found.

