Object Types, Properties, and Result Value Types
-----------------------------------------------

.. note::
   This section was generated from a live model by creating temporary elements where possible.
   For object types that cannot be inserted directly, no value-type inference is shown.

AGSN_HydraulicProfile
^^^^^^^^^^^^^^^^^^^^^

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

AirVessel
^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ````
   * - ``Beschreibung``
     - ````
   * - ``Indatab``
     - ````
   * - ``A``
     - ````
   * - ``Hb``
     - ````
   * - ``Vg0``
     - ````
   * - ``Pg0``
     - ````
   * - ``Tgas``
     - ````
   * - ``Fkatab``
     - ````
   * - ``Dn``
     - ````
   * - ``Zetapos``
     - ````
   * - ``Zetaneg``
     - ````
   * - ``Rgas``
     - ````
   * - ``Rpoly``
     - ````
   * - ``Ibla``
     - ````
   * - ``Knotk``
     - ````
   * - ``Zkor``
     - ````
   * - ``Fkfstf``
     - ````
   * - ``Fkcont``
     - ````
   * - ``Idreferenz``
     - ````
   * - ``Iplanung``
     - ````
   * - ``Tk``
     - ````
   * - ``Pk``
     - ````
   * - ``InVariant``
     - ````
   * - ``GeometriesDiffer``
     - ````
   * - ``SymbolGraf``
     - ````
   * - ``SymbolFactor``
     - ````
   * - ``Xkor``
     - ````
   * - ``Ykor``
     - ````
   * - ``Angle``
     - ````
   * - ``bz.Fk``
     - ````

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``HLUFT``
     - ````
   * - ``IAKTIV``
     - ````
   * - ``M``
     - ````
   * - ``MAINELEMENT``
     - ````
   * - ``PLUFT``
     - ````
   * - ``QM``
     - ````
   * - ``RHO``
     - ````
   * - ``T``
     - ````
   * - ``V``
     - ````
   * - ``VOL``
     - ````
   * - ``VOLDA``
     - ````
   * - ``VOLGAS``
     - ````
   * - ``WALTER``
     - ````
   * - ``WST``
     - ````

Arrow
^^^^^

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

Atmosphere
^^^^^^^^^^

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

BlockConnectionNode
^^^^^^^^^^^^^^^^^^^

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

CalcPari
^^^^^^^^

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

CharacteristicLossTable
^^^^^^^^^^^^^^^^^^^^^^^

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

CharacteristicLossTable_Row
^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

Circle
^^^^^^

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

Compressor
^^^^^^^^^^

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
   * - ``Fkkomk``
     - ``string``
   * - ``Inda``
     - ``int32``
   * - ``Etam``
     - ``single``
   * - ``Tfahraus``
     - ``single``
   * - ``Tfahrein``
     - ``single``
   * - ``Dndt``
     - ``single``
   * - ``Dqndt``
     - ``single``
   * - ``Dpdt``
     - ``single``
   * - ``Ipverh``
     - ``int32``
   * - ``Pverhqn``
     - ``single``
   * - ``Pverhdp``
     - ``single``
   * - ``Etat``
     - ``single``
   * - ``Ibrenng``
     - ``int32``
   * - ``Iprst``
     - ``int32``
   * - ``Fkantp``
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
   * - ``bz.Inds``
     - ``int32``
   * - ``bz.Sw``
     - ``single``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``DP``
     - ````
   * - ``DT``
     - ````
   * - ``EINAUS``
     - ````
   * - ``ETAP``
     - ````
   * - ``IAKTIV``
     - ````
   * - ``IND``
     - ````
   * - ``INDANT``
     - ````
   * - ``M``
     - ````
   * - ``MAINELEMENT``
     - ````
   * - ``N``
     - ````
   * - ``P``
     - ````
   * - ``PE``
     - ````
   * - ``PI``
     - ````
   * - ``PK``
     - ``string``
   * - ``PMAX``
     - ````
   * - ``PRATIO``
     - ````
   * - ``QN``
     - ````
   * - ``QNBG``
     - ````
   * - ``QNGES``
     - ````
   * - ``TI``
     - ````
   * - ``TK``
     - ``string``
   * - ``YP``
     - ````

CompressorTable
^^^^^^^^^^^^^^^

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

CompressorTable_Row
^^^^^^^^^^^^^^^^^^^

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

ControlEngineeringNexus
^^^^^^^^^^^^^^^^^^^^^^^

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

ControlMode
^^^^^^^^^^^

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
     - Value Type
   * - ``MAINELEMENT``
     - ````
   * - ``RCPL``
     - ````
   * - ``SWVT``
     - ````
   * - ``W``
     - ````

ControlPointTable
^^^^^^^^^^^^^^^^^

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
     - Value Type
   * - ``KNOT``
     - ````
   * - ``MAINELEMENT``
     - ````
   * - ``W``
     - ````
   * - ``X``
     - ````
   * - ``XD``
     - ````

ControlPointTable_Row
^^^^^^^^^^^^^^^^^^^^^

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
     - Value Type
   * - ``MAINELEMENT``
     - ````
   * - ``W``
     - ``single``
   * - ``X``
     - ````
   * - ``XD``
     - ````

ControlValve
^^^^^^^^^^^^

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
     - Value Type
   * - ``DH``
     - ````
   * - ``DP``
     - ````
   * - ``DPH``
     - ````
   * - ``DSI``
     - ````
   * - ``DSK``
     - ````
   * - ``FS``
     - ````
   * - ``HR``
     - ````
   * - ``IAKTIV``
     - ````
   * - ``INDSTD``
     - ````
   * - ``KV``
     - ````
   * - ``M``
     - ````
   * - ``MAINELEMENT``
     - ````
   * - ``PHI``
     - ````
   * - ``PR``
     - ````
   * - ``Q2``
     - ````
   * - ``QM``
     - ````
   * - ``RART``
     - ````
   * - ``RHO``
     - ````
   * - ``V``
     - ````
   * - ``W``
     - ````
   * - ``X``
     - ````
   * - ``ZETA``
     - ````

ControlVariableConverter
^^^^^^^^^^^^^^^^^^^^^^^^

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
     - Value Type
   * - ``LFKT``
     - ````
   * - ``MAINELEMENT``
     - ````
   * - ``PHI1``
     - ````
   * - ``PUMD``
     - ````
   * - ``PVAR``
     - ````
   * - ``QVAR``
     - ````
   * - ``SWVT``
     - ````
   * - ``TEVT``
     - ````
   * - ``TRGCOUNT``
     - ````
   * - ``WEVT``
     - ````
   * - ``XE1``
     - ````
   * - ``XE2``
     - ````

ControlVariableConverterRSTE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
     - Value Type
   * - ``DYDT1``
     - ````
   * - ``DYDT2``
     - ````
   * - ``DYDT3``
     - ````
   * - ``DYDT4``
     - ````
   * - ``DYDT5``
     - ````
   * - ``MAINELEMENT``
     - ````
   * - ``XE1``
     - ````
   * - ``YS1``
     - ````
   * - ``YS2``
     - ````
   * - ``YS3``
     - ````
   * - ``YS4``
     - ````
   * - ``YS5``
     - ````

CrossSectionTable
^^^^^^^^^^^^^^^^^

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

CrossSectionTable_Row
^^^^^^^^^^^^^^^^^^^^^

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

DPGR_DPKT_DatapointDpgrConnection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

DPGR_DataPointGroup
^^^^^^^^^^^^^^^^^^^

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

DPKT_Datapoint
^^^^^^^^^^^^^^

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

DamageRatesTable
^^^^^^^^^^^^^^^^

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

DamageRatesTable_Row
^^^^^^^^^^^^^^^^^^^^

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

DeadTimeElement
^^^^^^^^^^^^^^^

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
     - Value Type
   * - ``MAINELEMENT``
     - ````
   * - ``XA``
     - ````
   * - ``XE``
     - ````

Demand
^^^^^^

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

DifferentialRegulator
^^^^^^^^^^^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ````
   * - ``Beschreibung``
     - ````
   * - ``Dn``
     - ````
   * - ``Typ``
     - ````
   * - ``Fkkref1``
     - ````
   * - ``Fkkref2``
     - ````
   * - ``Fkzep1``
     - ````
   * - ``Ts``
     - ````
   * - ``Fkcont``
     - ````
   * - ``Idreferenz``
     - ````
   * - ``Iplanung``
     - ````
   * - ``Tk``
     - ````
   * - ``Pk``
     - ````
   * - ``InVariant``
     - ````
   * - ``Xkor``
     - ````
   * - ``Ykor``
     - ````
   * - ``ShowDescription``
     - ````
   * - ``PositionOfDescription``
     - ````
   * - ``Angle``
     - ````
   * - ``SymbolFactor``
     - ````
   * - ``GeometriesDiffer``
     - ````
   * - ``bz.Fk``
     - ````
   * - ``bz.Fkswvt``
     - ````
   * - ``bz.Dphsoll``
     - ````
   * - ``bz.Indsoll``
     - ````

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``DH``
     - ````
   * - ``DP``
     - ````
   * - ``DPH``
     - ````
   * - ``DPHSOLL``
     - ````
   * - ``DPSOLL``
     - ````
   * - ``DSI``
     - ````
   * - ``DSK``
     - ````
   * - ``FS``
     - ````
   * - ``HR``
     - ````
   * - ``IAKTIV``
     - ````
   * - ``KV``
     - ````
   * - ``M``
     - ````
   * - ``MAINELEMENT``
     - ````
   * - ``PHI``
     - ````
   * - ``PR``
     - ````
   * - ``QM``
     - ````
   * - ``RHO``
     - ````
   * - ``SWVT``
     - ````
   * - ``V``
     - ````
   * - ``ZETA``
     - ````

DirectionalArrow
^^^^^^^^^^^^^^^^

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

DistrictHeatingConsumer
^^^^^^^^^^^^^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ````
   * - ``Beschreibung``
     - ````
   * - ``Ind0``
     - ````
   * - ``W0``
     - ````
   * - ``Qm0``
     - ````
   * - ``Tvl0``
     - ````
   * - ``Trs0``
     - ````
   * - ``Lfk``
     - ````
   * - ``Rho0``
     - ````
   * - ``Dtmin``
     - ````
   * - ``Indtr``
     - ````
   * - ``Trsk``
     - ````
   * - ``Fktrft``
     - ````
   * - ``A``
     - ````
   * - ``B``
     - ````
   * - ``C``
     - ````
   * - ``Vtyp``
     - ````
   * - ``V0``
     - ````
   * - ``P1soll``
     - ````
   * - ``Dpvlmin``
     - ````
   * - ``Fkzep1vl``
     - ````
   * - ``Tsvl``
     - ````
   * - ``Zevk``
     - ````
   * - ``Dphaus``
     - ````
   * - ``Dprlmin``
     - ````
   * - ``Fkzep1rl``
     - ````
   * - ``Tsrl``
     - ````
   * - ``Imbg``
     - ````
   * - ``Irfv``
     - ````
   * - ``Fkcont``
     - ````
   * - ``Idreferenz``
     - ````
   * - ``Iplanung``
     - ````
   * - ``CPM``
     - ````
   * - ``NumberOfVERB``
     - ````
   * - ``IndtrKlartext``
     - ````
   * - ``M0Estimated``
     - ````
   * - ``W0Estimated``
     - ````
   * - ``Tk``
     - ````
   * - ``Pk``
     - ````
   * - ``InVariant``
     - ````
   * - ``Xkor``
     - ````
   * - ``Ykor``
     - ````
   * - ``ShowDescription``
     - ````
   * - ``PositionOfDescription``
     - ````
   * - ``Angle``
     - ````
   * - ``SymbolFactor``
     - ````
   * - ``GeometriesDiffer``
     - ````
   * - ``bz.Fk``
     - ````
   * - ``bz.Indlast``
     - ````
   * - ``bz.Indlfkt2``
     - ````
   * - ``bz.Fklfkt``
     - ````
   * - ``bz.Fklfkt2``
     - ````
   * - ``bz.Fkqvar``
     - ````
   * - ``bz.Fktevt``
     - ````
   * - ``bz.IndlastKlartext``
     - ````

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``DH``
     - ````
   * - ``DP``
     - ````
   * - ``DPH``
     - ````
   * - ``IAKTIV``
     - ````
   * - ``INDUV``
     - ````
   * - ``LFH``
     - ````
   * - ``LFKT``
     - ````
   * - ``LFT``
     - ````
   * - ``M``
     - ````
   * - ``MAINELEMENT``
     - ````
   * - ``MHYUV``
     - ````
   * - ``MSOLL``
     - ````
   * - ``MTHUV``
     - ````
   * - ``P1``
     - ````
   * - ``P2``
     - ````
   * - ``P3``
     - ````
   * - ``PH1``
     - ````
   * - ``PH2``
     - ````
   * - ``PH3``
     - ````
   * - ``PHIRL``
     - ````
   * - ``PHIVL``
     - ````
   * - ``QM``
     - ````
   * - ``QM13``
     - ````
   * - ``QM31``
     - ````
   * - ``QMI``
     - ````
   * - ``QMK``
     - ````
   * - ``QVAR``
     - ````
   * - ``RHOI``
     - ````
   * - ``RHOK``
     - ````
   * - ``TI``
     - ````
   * - ``TK``
     - ````
   * - ``TVMIN``
     - ````
   * - ``W``
     - ````
   * - ``WHYUV``
     - ````
   * - ``WSOLL``
     - ````
   * - ``WTHUV``
     - ````

DistrictHeatingFeeder
^^^^^^^^^^^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ````
   * - ``Beschreibung``
     - ````
   * - ``Dn``
     - ````
   * - ``Zeta``
     - ````
   * - ``Taus``
     - ````
   * - ``Irueck``
     - ````
   * - ``Fkcont``
     - ````
   * - ``Idreferenz``
     - ````
   * - ``Iplanung``
     - ````
   * - ``Tk``
     - ````
   * - ``Pk``
     - ````
   * - ``InVariant``
     - ````
   * - ``Xkor``
     - ````
   * - ``Ykor``
     - ````
   * - ``ShowDescription``
     - ````
   * - ``PositionOfDescription``
     - ````
   * - ``Angle``
     - ````
   * - ``SymbolFactor``
     - ````
   * - ``GeometriesDiffer``
     - ````
   * - ``bz.Fk``
     - ````
   * - ``bz.Ihytyp``
     - ````
   * - ``bz.Ithtyp``
     - ````
   * - ``bz.Tkon``
     - ````
   * - ``bz.Fktevt``
     - ````
   * - ``bz.Wkon``
     - ````
   * - ``bz.Fkwevt``
     - ````
   * - ``bz.IhytypKlartext``
     - ````
   * - ``bz.IthtypKlartext``
     - ````

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``DH``
     - ````
   * - ``DP``
     - ````
   * - ``DPH``
     - ````
   * - ``IAKTIV``
     - ````
   * - ``IHYTYP``
     - ````
   * - ``ITHTYP``
     - ````
   * - ``M``
     - ````
   * - ``MAINELEMENT``
     - ````
   * - ``QM``
     - ````
   * - ``RHOI``
     - ````
   * - ``RHOK``
     - ````
   * - ``TEVT``
     - ````
   * - ``TI``
     - ````
   * - ``TK``
     - ````
   * - ``TKON``
     - ````
   * - ``V``
     - ````
   * - ``W``
     - ````
   * - ``W0``
     - ````
   * - ``WEVT``
     - ````
   * - ``WSOLL``
     - ````

Divider
^^^^^^^

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
     - Value Type
   * - ``MAINELEMENT``
     - ````
   * - ``XA``
     - ````
   * - ``XE1``
     - ````
   * - ``XE2``
     - ````

DriveEfficiencyTable
^^^^^^^^^^^^^^^^^^^^

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

DriveEfficiencyTable_Row
^^^^^^^^^^^^^^^^^^^^^^^^

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

DrivePowerTable
^^^^^^^^^^^^^^^

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

DrivePowerTable_Row
^^^^^^^^^^^^^^^^^^^

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

EBES_FeederGroups
^^^^^^^^^^^^^^^^^

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

EfficiencyConverterTable
^^^^^^^^^^^^^^^^^^^^^^^^

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

EfficiencyConverterTable_Row
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

ElementQuery
^^^^^^^^^^^^

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

EnergyRecoveryTable
^^^^^^^^^^^^^^^^^^^

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

EnergyRecoveryTable_Row
^^^^^^^^^^^^^^^^^^^^^^^

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

EnvironmentTemp
^^^^^^^^^^^^^^^

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

FWBZ_DistrictHeatingReferenceValues
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

FlapValve
^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ````
   * - ``Beschreibung``
     - ````
   * - ``Dn``
     - ````
   * - ``Fkphiv``
     - ````
   * - ``Fkzep2``
     - ````
   * - ``Ts``
     - ````
   * - ``Phie``
     - ````
   * - ``Te``
     - ````
   * - ``Fkcont``
     - ````
   * - ``Idreferenz``
     - ````
   * - ``Iplanung``
     - ````
   * - ``Tk``
     - ````
   * - ``Pk``
     - ````
   * - ``InVariant``
     - ````
   * - ``Xkor``
     - ````
   * - ``Ykor``
     - ````
   * - ``ShowDescription``
     - ````
   * - ``PositionOfDescription``
     - ````
   * - ``Angle``
     - ````
   * - ``SymbolFactor``
     - ````
   * - ``GeometriesDiffer``
     - ````
   * - ``bz.Fk``
     - ````

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``DH``
     - ````
   * - ``DP``
     - ````
   * - ``DSI``
     - ````
   * - ``DSK``
     - ````
   * - ``FS``
     - ````
   * - ``HR``
     - ````
   * - ``IAKTIV``
     - ````
   * - ``KV``
     - ````
   * - ``M``
     - ````
   * - ``MAINELEMENT``
     - ````
   * - ``PHI``
     - ````
   * - ``PHR``
     - ````
   * - ``PR``
     - ````
   * - ``QM``
     - ````
   * - ``RHO``
     - ````
   * - ``V``
     - ````
   * - ``ZETA``
     - ````

FlowControlUnit
^^^^^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ````
   * - ``Beschreibung``
     - ````
   * - ``Dn``
     - ````
   * - ``Fkzep1``
     - ````
   * - ``Tsig``
     - ````
   * - ``Dqdt``
     - ````
   * - ``Tvoll``
     - ````
   * - ``Fkcont``
     - ````
   * - ``Idreferenz``
     - ````
   * - ``Iplanung``
     - ````
   * - ``Tk``
     - ````
   * - ``Pk``
     - ````
   * - ``InVariant``
     - ````
   * - ``Xkor``
     - ````
   * - ``Ykor``
     - ````
   * - ``ShowDescription``
     - ````
   * - ``PositionOfDescription``
     - ````
   * - ``Angle``
     - ````
   * - ``SymbolFactor``
     - ````
   * - ``GeometriesDiffer``
     - ````
   * - ``bz.Fk``
     - ````
   * - ``bz.Indsoll``
     - ````
   * - ``bz.Qmsoll``
     - ````
   * - ``bz.Fkswvtqm``
     - ````
   * - ``bz.Phisoll``
     - ````
   * - ``bz.Fkswvtphi``
     - ````

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``DH``
     - ````
   * - ``DP``
     - ````
   * - ``DPH``
     - ````
   * - ``DSI``
     - ````
   * - ``DSK``
     - ````
   * - ``FS``
     - ````
   * - ``HR``
     - ````
   * - ``IAKTIV``
     - ````
   * - ``IND``
     - ````
   * - ``KV``
     - ````
   * - ``M``
     - ````
   * - ``MAINELEMENT``
     - ````
   * - ``PHI``
     - ````
   * - ``PHISOLL``
     - ````
   * - ``PR``
     - ````
   * - ``Q``
     - ````
   * - ``QM``
     - ````
   * - ``QMSOLL``
     - ````
   * - ``RHO``
     - ````
   * - ``SWVTPHI``
     - ````
   * - ``SWVTQM``
     - ````
   * - ``V``
     - ````
   * - ``ZETA``
     - ````

FluidQualityParamSet
^^^^^^^^^^^^^^^^^^^^

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
     - Value Type
   * - ``MAINELEMENT``
     - ````
   * - ``SWVTCHLORID``
     - ````
   * - ``SWVTEISENFILT``
     - ````
   * - ``SWVTEISENGES``
     - ````
   * - ``SWVTHI``
     - ````
   * - ``SWVTHS``
     - ````
   * - ``SWVTLEITFAEH``
     - ````
   * - ``SWVTMN``
     - ````
   * - ``SWVTPHWERT``
     - ````
   * - ``SWVTRHON``
     - ````
   * - ``SWVTSULFAT``
     - ````
   * - ``SWVTTEMP``
     - ````

FluidQualityParamSet_OS
^^^^^^^^^^^^^^^^^^^^^^^

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

FluidThermalPropertyGroup
^^^^^^^^^^^^^^^^^^^^^^^^^

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

FreeDuct
^^^^^^^^

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
     - Value Type
   * - ``MAINELEMENT``
     - ````
   * - ``OA``
     - ````
   * - ``OW``
     - ````
   * - ``UA``
     - ````
   * - ``UW``
     - ````
   * - ``WERT``
     - ````

FunctionGenerator
^^^^^^^^^^^^^^^^^

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
     - Value Type
   * - ``LFKT``
     - ````
   * - ``MAINELEMENT``
     - ````
   * - ``XA``
     - ````
   * - ``XE``
     - ````

FunctionTable
^^^^^^^^^^^^^

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

FunctionTable_Row
^^^^^^^^^^^^^^^^^

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

GasComponent
^^^^^^^^^^^^

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

GasMixture
^^^^^^^^^^

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

GeneralSection
^^^^^^^^^^^^^^

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
     - Value Type
   * - ``CPUTIME``
     - ````
   * - ``CVERSO``
     - ````
   * - ``EXSTAT``
     - ````
   * - ``FWVB_DPHMIN``
     - ````
   * - ``FWVB_TVLMIN``
     - ````
   * - ``INTERAKTRG``
     - ````
   * - ``INTERAKTTH``
     - ````
   * - ``ITERHY``
     - ````
   * - ``ITERTH``
     - ````
   * - ``JWARN``
     - ````
   * - ``KNOT_PHMAX``
     - ````
   * - ``KNOT_PHMAX_R``
     - ````
   * - ``KNOT_PHMAX_U``
     - ````
   * - ``KNOT_PHMAX_V``
     - ````
   * - ``KNOT_PHMIN``
     - ````
   * - ``KNOT_PHMIN_R``
     - ````
   * - ``KNOT_PHMIN_U``
     - ````
   * - ``KNOT_PHMIN_V``
     - ````
   * - ``LFQSV``
     - ````
   * - ``LINEPACKGEOM``
     - ````
   * - ``LINEPACKGES``
     - ````
   * - ``LINEPACKRATE``
     - ````
   * - ``MAINELEMENT``
     - ````
   * - ``MFVHYUV``
     - ````
   * - ``MFVTHUV``
     - ````
   * - ``MKNUV``
     - ````
   * - ``NETZABN``
     - ````
   * - ``NETZABNEXITS``
     - ````
   * - ``NETZBEZ``
     - ````
   * - ``NFEHL``
     - ````
   * - ``NFVHYUV``
     - ````
   * - ``NFVTHUV``
     - ````
   * - ``NKNUV``
     - ````
   * - ``NMELD``
     - ````
   * - ``NPGREST``
     - ````
   * - ``NWARN``
     - ````
   * - ``PAV``
     - ````
   * - ``RHOAV``
     - ````
   * - ``SNAPSHOTTYPE``
     - ````
   * - ``TAV``
     - ````
   * - ``TIMESTAMP``
     - ````
   * - ``TVMINMAX``
     - ````
   * - ``USRTIME``
     - ````

Gravitation
^^^^^^^^^^^

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

HeatExchanger
^^^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ````
   * - ``Beschreibung``
     - ````
   * - ``W0``
     - ````
   * - ``T1ein0``
     - ````
   * - ``T1aus0``
     - ````
   * - ``T2ein0``
     - ````
   * - ``T2aus0``
     - ````
   * - ``Dn``
     - ````
   * - ``Dp10min``
     - ````
   * - ``Inddprl``
     - ````
   * - ``Fkzep1rl``
     - ````
   * - ``Tsrl``
     - ````
   * - ``Dp20``
     - ````
   * - ``Re0``
     - ````
   * - ``Expert``
     - ````
   * - ``A``
     - ````
   * - ``K``
     - ````
   * - ``Alpha1``
     - ````
   * - ``Alpha2``
     - ````
   * - ``L1``
     - ````
   * - ``L2``
     - ````
   * - ``Indwue``
     - ````
   * - ``Kstrant``
     - ````
   * - ``Fkfwvb``
     - ````
   * - ``Fkfwes``
     - ````
   * - ``Fkcont``
     - ````
   * - ``Idreferenz``
     - ````
   * - ``Iplanung``
     - ````
   * - ``Tk``
     - ````
   * - ``Pk``
     - ````
   * - ``InVariant``
     - ````
   * - ``Xkor``
     - ````
   * - ``Ykor``
     - ````
   * - ``ShowDescription``
     - ````
   * - ``PositionOfDescription``
     - ````
   * - ``Angle``
     - ````
   * - ``SymbolFactor``
     - ````
   * - ``GeometriesDiffer``
     - ````
   * - ``bz.Fk``
     - ````
   * - ``bz.Einaus``
     - ````
   * - ``bz.Ithtyp``
     - ````
   * - ``bz.T2aus``
     - ````
   * - ``bz.Fktevt``
     - ````

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``AKTIV``
     - ````
   * - ``C1``
     - ````
   * - ``C2``
     - ````
   * - ``EPS1``
     - ````
   * - ``EPS2``
     - ````
   * - ``IAKTIV``
     - ````
   * - ``INDUV``
     - ````
   * - ``KA``
     - ````
   * - ``MAINELEMENT``
     - ````
   * - ``NTU1``
     - ````
   * - ``NTU2``
     - ````
   * - ``NU1``
     - ````
   * - ``NU2``
     - ````
   * - ``PR1``
     - ````
   * - ``PR2``
     - ````
   * - ``Q``
     - ````
   * - ``RE1``
     - ````
   * - ``RE2``
     - ````
   * - ``T1AUS``
     - ````
   * - ``T1EIN``
     - ````
   * - ``T2AUS``
     - ````
   * - ``T2EIN``
     - ````
   * - ``THETA``
     - ````
   * - ``TMLOG``
     - ````
   * - ``W1``
     - ````
   * - ``W2``
     - ````

HeatFeederConsumerStation
^^^^^^^^^^^^^^^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ````
   * - ``Beschreibung``
     - ````
   * - ``Fkfwes``
     - ````
   * - ``Fkfwvb``
     - ````
   * - ``Fkpreg``
     - ````
   * - ``Fkpump``
     - ````
   * - ``Fkklap``
     - ````
   * - ``Indusing``
     - ````
   * - ``Dn``
     - ````
   * - ``Dpvb0min``
     - ````
   * - ``Dpes0``
     - ````
   * - ``PuQmref``
     - ````
   * - ``PuNref``
     - ````
   * - ``PuHref``
     - ````
   * - ``PuPref``
     - ````
   * - ``Volsp``
     - ````
   * - ``HMantel``
     - ````
   * - ``HWsOkDif``
     - ````
   * - ``HDif``
     - ````
   * - ``HBUkDif``
     - ````
   * - ``RInnen``
     - ````
   * - ``RDif``
     - ````
   * - ``HWsMax``
     - ````
   * - ``Dhbasis``
     - ````
   * - ``UMantel``
     - ````
   * - ``UBoden``
     - ````
   * - ``Tob``
     - ````
   * - ``Tu``
     - ````
   * - ``Tdr``
     - ````
   * - ``TrefMin``
     - ````
   * - ``TtolEs``
     - ````
   * - ``TtolVb``
     - ````
   * - ``W0Sp``
     - ````
   * - ``W0Es``
     - ````
   * - ``Tsp0``
     - ````
   * - ``Trl0``
     - ````
   * - ``W0Vb``
     - ````
   * - ``Tvl0``
     - ````
   * - ``Trs0``
     - ````
   * - ``Indtr``
     - ````
   * - ``Fktrft``
     - ````
   * - ``Fksoko``
     - ````
   * - ``Indtrack``
     - ````
   * - ``Medium``
     - ````
   * - ``Qfs``
     - ````
   * - ``Tgrenz``
     - ````
   * - ``Deta0bLost``
     - ````
   * - ``Abrutto``
     - ````
   * - ``Wcorr``
     - ````
   * - ``Indrohr``
     - ````
   * - ``Vrv``
     - ````
   * - ``Indrumg``
     - ````
   * - ``L``
     - ````
   * - ``Di``
     - ````
   * - ``Kr``
     - ````
   * - ``Rd``
     - ````
   * - ``Lambdad``
     - ````
   * - ``Lambdae``
     - ````
   * - ``He``
     - ````
   * - ``KrKt``
     - ````
   * - ``Tru``
     - ````
   * - ``Indwt``
     - ````
   * - ``Dtwt``
     - ````
   * - ``Indtset``
     - ````
   * - ``Gtmaxtset``
     - ````
   * - ``Dtsett``
     - ````
   * - ``PrDn``
     - ````
   * - ``Fkzep1Pr``
     - ````
   * - ``Fkcont``
     - ````
   * - ``Idreferenz``
     - ````
   * - ``Iplanung``
     - ````
   * - ``NodeNameI``
     - ````
   * - ``NodeNameK``
     - ````
   * - ``StorageType``
     - ````
   * - ``Tk``
     - ````
   * - ``Pk``
     - ````
   * - ``InVariant``
     - ````
   * - ``Xkor``
     - ````
   * - ``Ykor``
     - ````
   * - ``ShowDescription``
     - ````
   * - ``PositionOfDescription``
     - ````
   * - ``Angle``
     - ````
   * - ``SymbolFactor``
     - ````
   * - ``GeometriesDiffer``
     - ````
   * - ``bz.Fk``
     - ````
   * - ``bz.Einaus``
     - ````
   * - ``bz.IndsSp``
     - ````
   * - ``bz.ModeSp``
     - ````
   * - ``bz.Ithtyp``
     - ````
   * - ``bz.Indlast``
     - ````
   * - ``bz.Neigung``
     - ````
   * - ``bz.Azimut``
     - ````
   * - ``bz.Fkwttr``
     - ````
   * - ``bz.FktevtEs``
     - ````
   * - ``bz.FktevtRs``
     - ````
   * - ``bz.FkwevtSp``
     - ````
   * - ``bz.FkqvarSp``
     - ````
   * - ``bz.FkwevtEs``
     - ````
   * - ``bz.FkwevtVb``
     - ````
   * - ``bz.Fklfkt``
     - ````
   * - ``bz.Pvlmax``
     - ````
   * - ``bz.Ppumax``
     - ````
   * - ``bz.Indstagn``
     - ````
   * - ``bz.TzuMax``
     - ````
   * - ``bz.TzuMin``
     - ````
   * - ``bz.TspMin``
     - ````
   * - ``bz.TrsMax``
     - ````
   * - ``bz.W0SpMin``
     - ````
   * - ``bz.Qsprel0``
     - ````
   * - ``bz.HWsStart``
     - ````
   * - ``bz.TobStart``
     - ````
   * - ``bz.TuStart``
     - ````
   * - ``bz.TtolEval``
     - ````

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``DH_KALT``
     - ````
   * - ``DH_MIX``
     - ````
   * - ``DH_WARM``
     - ````
   * - ``DPH_ES``
     - ````
   * - ``DPH_VB``
     - ````
   * - ``DTLEER``
     - ````
   * - ``ETA_PU``
     - ````
   * - ``GGLOB``
     - ````
   * - ``GKOLL``
     - ````
   * - ``H_MIX``
     - ````
   * - ``H_PU``
     - ````
   * - ``H_WS``
     - ````
   * - ``IAKTIV``
     - ````
   * - ``MAINELEMENT``
     - ````
   * - ``MMAXBL``
     - ````
   * - ``MMAXEL``
     - ````
   * - ``MMIN``
     - ````
   * - ``N_PU``
     - ````
   * - ``P_PU``
     - ````
   * - ``Q_PU``
     - ````
   * - ``QM``
     - ````
   * - ``QM_ES``
     - ````
   * - ``QM_PR``
     - ````
   * - ``QM_VB``
     - ````
   * - ``QSP``
     - ````
   * - ``QSPREL``
     - ````
   * - ``QV_BODEN``
     - ````
   * - ``QV_DR``
     - ````
   * - ``QV_MANTEL``
     - ````
   * - ``QV_TOTAL``
     - ````
   * - ``T_KALT``
     - ````
   * - ``T_MIX``
     - ````
   * - ``T_WARM``
     - ````
   * - ``TDIFFO``
     - ````
   * - ``TDIFFU``
     - ````
   * - ``TRL``
     - ````
   * - ``TRS``
     - ````
   * - ``TSP``
     - ````
   * - ``TVEC``
     - ````
   * - ``TVL``
     - ````
   * - ``W``
     - ````
   * - ``W_ES``
     - ````
   * - ``W_FS``
     - ````
   * - ``W_PR``
     - ````
   * - ``W_RO``
     - ````
   * - ``W_VB``
     - ````
   * - ``WKOLL``
     - ````

HeaterCooler
^^^^^^^^^^^^

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
   * - ``Eta``
     - ``single``
   * - ``Dpnum``
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
   * - ``bz.Inds``
     - ``int32``
   * - ``bz.Sw``
     - ``single``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``EINAUS``
     - ````
   * - ``IAKTIV``
     - ````
   * - ``M``
     - ````
   * - ``MAINELEMENT``
     - ````
   * - ``P``
     - ````
   * - ``PE``
     - ````
   * - ``PI``
     - ````
   * - ``PK``
     - ``string``
   * - ``QN``
     - ````
   * - ``TI``
     - ````
   * - ``TK``
     - ``string``

Histeresis
^^^^^^^^^^

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
     - Value Type
   * - ``MAINELEMENT``
     - ````
   * - ``XA``
     - ````
   * - ``XE``
     - ````
   * - ``XO``
     - ``single``
   * - ``XU``
     - ``single``

House
^^^^^

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

Hydrant
^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ````
   * - ``Beschreibung``
     - ````
   * - ``Typ``
     - ````
   * - ``Zkor``
     - ````
   * - ``Zeta``
     - ````
   * - ``Dn``
     - ````
   * - ``FkdtroRowd``
     - ````
   * - ``L``
     - ````
   * - ``Rau``
     - ````
   * - ``Fkrohr``
     - ````
   * - ``Poskm``
     - ````
   * - ``Fkknot``
     - ````
   * - ``Idreferenz``
     - ````
   * - ``Xkor``
     - ````
   * - ``Ykor``
     - ````
   * - ``Tk``
     - ````
   * - ``Pk``
     - ````
   * - ``InVariant``
     - ````
   * - ``GeometriesDiffer``
     - ````
   * - ``Angle``
     - ````
   * - ``SymbolFactor``
     - ````
   * - ``bz.Fk``
     - ````
   * - ``bz.Phsoll``
     - ````
   * - ``bz.Qmsoll``
     - ````
   * - ``bz.Indi``
     - ````
   * - ``bz.Iaktiv``
     - ````
   * - ``bz.Fkswvt``
     - ````
   * - ``bz.PhMin``
     - ````

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``BCTYP``
     - ````
   * - ``IAKTIV``
     - ````
   * - ``MAINELEMENT``
     - ````
   * - ``PH_EINB``
     - ````
   * - ``PH_ENTN``
     - ````
   * - ``PH_MIN``
     - ````
   * - ``PHR``
     - ````
   * - ``PHR_ROHR``
     - ````
   * - ``PHSOLL``
     - ````
   * - ``QM``
     - ````
   * - ``QSOLL``
     - ````
   * - ``UV``
     - ````

Integrator
^^^^^^^^^^

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
     - Value Type
   * - ``MAINELEMENT``
     - ````
   * - ``XA``
     - ````
   * - ``XE``
     - ````

LAYR_Layer
^^^^^^^^^^

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

LoadFactorTable
^^^^^^^^^^^^^^^

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
     - Value Type
   * - ``FWVB_DPHMIN``
     - ````
   * - ``FWVB_TVLMIN``
     - ````
   * - ``LF``
     - ````
   * - ``MAINELEMENT``
     - ````
   * - ``MFVHYUV``
     - ````
   * - ``MFVTHUV``
     - ````
   * - ``NFVHYUV``
     - ````
   * - ``NFVTHUV``
     - ````
   * - ``TVMINMAX``
     - ````

LoadFactorTable_Row
^^^^^^^^^^^^^^^^^^^

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

LogicalComparison
^^^^^^^^^^^^^^^^^

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
     - Value Type
   * - ``MAINELEMENT``
     - ````
   * - ``XA``
     - ````
   * - ``XE1``
     - ````
   * - ``XE2``
     - ````

LogicalStorage
^^^^^^^^^^^^^^

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
     - Value Type
   * - ``MAINELEMENT``
     - ````
   * - ``XA``
     - ````
   * - ``XE1``
     - ````
   * - ``XE2``
     - ````

MeasuredVariableTable
^^^^^^^^^^^^^^^^^^^^^

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
     - Value Type
   * - ``MAINELEMENT``
     - ````
   * - ``W``
     - ````

MeasuredVariableTable_Row
^^^^^^^^^^^^^^^^^^^^^^^^^

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

MinMaxSelection
^^^^^^^^^^^^^^^

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
     - Value Type
   * - ``MAINELEMENT``
     - ````
   * - ``XA``
     - ````
   * - ``XE1``
     - ````
   * - ``XE2``
     - ````

Multiplier
^^^^^^^^^^

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
     - Value Type
   * - ``MAINELEMENT``
     - ````
   * - ``MULT``
     - ````
   * - ``XA``
     - ````
   * - ``XE1``
     - ````
   * - ``XE2``
     - ````

NetValve
^^^^^^^^

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
     - Value Type
   * - ``MAINELEMENT``
     - ````
   * - ``STELLUNG``
     - ````

Node
^^^^

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
     - Value Type
   * - ``BCIND``
     - ````
   * - ``BCIND_CALC``
     - ````
   * - ``BCIND_FLOW``
     - ````
   * - ``BCIND_MODEL``
     - ````
   * - ``BCIND_SOURCE``
     - ````
   * - ``BCIND_TYPE``
     - ````
   * - ``CHLORID``
     - ````
   * - ``CP``
     - ````
   * - ``DP``
     - ````
   * - ``DPH``
     - ````
   * - ``DYNVISKO``
     - ````
   * - ``EH``
     - ````
   * - ``EISENFILT``
     - ````
   * - ``EISENGES``
     - ````
   * - ``ESQUELLSP``
     - ````
   * - ``FITT_ANGLE``
     - ````
   * - ``FITT_BASTYPE``
     - ````
   * - ``FITT_DP1``
     - ````
   * - ``FITT_DP2``
     - ````
   * - ``FITT_DP3``
     - ````
   * - ``FITT_STATE``
     - ````
   * - ``FITT_SUBTYPE``
     - ````
   * - ``FITT_VBTYPE1``
     - ````
   * - ``FITT_VBTYPE2``
     - ````
   * - ``FITT_VBTYPE3``
     - ````
   * - ``FITT_ZETA1``
     - ````
   * - ``FITT_ZETA2``
     - ````
   * - ``FITT_ZETA3``
     - ````
   * - ``FSTF_NAME``
     - ````
   * - ``GMIX_NAME``
     - ````
   * - ``H``
     - ````
   * - ``HI``
     - ````
   * - ``HMAX_INST``
     - ````
   * - ``HMIN_INST``
     - ````
   * - ``HS``
     - ````
   * - ``IAKTIV``
     - ````
   * - ``INDUV``
     - ````
   * - ``K``
     - ````
   * - ``KP``
     - ````
   * - ``KT``
     - ````
   * - ``LEITFAEH``
     - ````
   * - ``LFAKTAKT``
     - ````
   * - ``LFKT``
     - ````
   * - ``M``
     - ````
   * - ``MAINELEMENT``
     - ````
   * - ``MN``
     - ````
   * - ``P``
     - ````
   * - ``PDAMPF``
     - ````
   * - ``PH``
     - ````
   * - ``PH_EIN``
     - ````
   * - ``PH_MIN``
     - ````
   * - ``PHMINMAXDIF``
     - ````
   * - ``PHWERT``
     - ````
   * - ``PMAX_INST``
     - ````
   * - ``PMIN_INST``
     - ````
   * - ``PVAR``
     - ````
   * - ``Q2``
     - ````
   * - ``QM``
     - ````
   * - ``QMABS``
     - ````
   * - ``QVAR``
     - ````
   * - ``RHO``
     - ````
   * - ``RHON``
     - ````
   * - ``RHONQUAL``
     - ````
   * - ``SULFAT``
     - ````
   * - ``T``
     - ````
   * - ``TE``
     - ````
   * - ``TEMP``
     - ````
   * - ``TMAX_INST``
     - ````
   * - ``TMIN_INST``
     - ````
   * - ``TTR``
     - ````
   * - ``VOLD``
     - ````
   * - ``WALTER``
     - ````
   * - ``ZHKNR``
     - ````

NonReturnValvesTable
^^^^^^^^^^^^^^^^^^^^

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

NonReturnValvesTable_Row
^^^^^^^^^^^^^^^^^^^^^^^^

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

NumericalDisplay
^^^^^^^^^^^^^^^^

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

ObjectContainerSymbol
^^^^^^^^^^^^^^^^^^^^^

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

OpenContainer
^^^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ````
   * - ``Beschreibung``
     - ````
   * - ``Indatab``
     - ````
   * - ``A``
     - ````
   * - ``Hb``
     - ````
   * - ``Fkatab``
     - ````
   * - ``Dn``
     - ````
   * - ``Zetapos``
     - ````
   * - ``Zetaneg``
     - ````
   * - ``Knotk``
     - ````
   * - ``Zkor``
     - ````
   * - ``Fkfstf``
     - ````
   * - ``Fkknotfilling``
     - ````
   * - ``Filling``
     - ````
   * - ``Fkcont``
     - ````
   * - ``Idreferenz``
     - ````
   * - ``Iplanung``
     - ````
   * - ``Tk``
     - ````
   * - ``Pk``
     - ````
   * - ``InVariant``
     - ````
   * - ``GeometriesDiffer``
     - ````
   * - ``SymbolGraf``
     - ````
   * - ``SymbolFactor``
     - ````
   * - ``Xkor``
     - ````
   * - ``Ykor``
     - ````
   * - ``Angle``
     - ````
   * - ``bz.Fk``
     - ````
   * - ``bz.Wsp``
     - ````
   * - ``bz.Walter0``
     - ````
   * - ``bz.Tm0``
     - ````
   * - ``bz.WspNN``
     - ````

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``DWST_DT``
     - ````
   * - ``IAKTIV``
     - ````
   * - ``M``
     - ````
   * - ``MAINELEMENT``
     - ````
   * - ``MEXT``
     - ````
   * - ``QM``
     - ````
   * - ``QMEXT``
     - ````
   * - ``RHO``
     - ````
   * - ``T``
     - ````
   * - ``T0``
     - ````
   * - ``V``
     - ````
   * - ``VOL``
     - ````
   * - ``WALTER``
     - ````
   * - ``WALTER0``
     - ````
   * - ``WST``
     - ````
   * - ``WST0``
     - ````

Oval
^^^^

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

PARZ_TransientCalculationParameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

PhaseSeparation
^^^^^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ````
   * - ``Beschreibung``
     - ````
   * - ``Dn``
     - ````
   * - ``Zeta``
     - ````
   * - ``Fkcont``
     - ````
   * - ``Idreferenz``
     - ````
   * - ``Iplanung``
     - ````
   * - ``Tk``
     - ````
   * - ``Pk``
     - ````
   * - ``InVariant``
     - ````
   * - ``Xkor``
     - ````
   * - ``Ykor``
     - ````
   * - ``ShowDescription``
     - ````
   * - ``PositionOfDescription``
     - ````
   * - ``Angle``
     - ````
   * - ``SymbolFactor``
     - ````
   * - ``GeometriesDiffer``
     - ````
   * - ``bz.Fk``
     - ````

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``DH``
     - ````
   * - ``DP``
     - ````
   * - ``IAKTIV``
     - ````
   * - ``MAINELEMENT``
     - ````
   * - ``MI``
     - ````
   * - ``MK``
     - ````
   * - ``Q``
     - ````
   * - ``QM``
     - ````
   * - ``RHOI``
     - ````
   * - ``RHOK``
     - ````
   * - ``V``
     - ````

PidController
^^^^^^^^^^^^^

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
     - Value Type
   * - ``DYDT``
     - ````
   * - ``DYDTD``
     - ````
   * - ``DYDTI``
     - ````
   * - ``DYDTP``
     - ````
   * - ``MAINELEMENT``
     - ````
   * - ``XA``
     - ````
   * - ``XE1``
     - ````
   * - ``XE2``
     - ````

Pipe
^^^^

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
     - Value Type
   * - ``A``
     - ````
   * - ``ACALC``
     - ````
   * - ``CPI``
     - ````
   * - ``CPK``
     - ````
   * - ``DH``
     - ````
   * - ``DP``
     - ````
   * - ``DRAGRED``
     - ````
   * - ``DRAKONZ``
     - ````
   * - ``DSI``
     - ````
   * - ``DSK``
     - ````
   * - ``DTTR``
     - ````
   * - ``DWVERL``
     - ````
   * - ``DWVERLABS``
     - ````
   * - ``ETAAV``
     - ````
   * - ``FS``
     - ````
   * - ``HR``
     - ````
   * - ``HVEC``
     - ````
   * - ``IAKTIV``
     - ````
   * - ``IRTRENN``
     - ````
   * - ``JV``
     - ````
   * - ``JV2``
     - ````
   * - ``LAMBDA``
     - ````
   * - ``LECKEINAUS``
     - ````
   * - ``LECKMENGE``
     - ````
   * - ``LECKORT``
     - ````
   * - ``LINEPACK``
     - ````
   * - ``LINEPACKGEOM``
     - ````
   * - ``LINEPACKRATE``
     - ````
   * - ``MAINELEMENT``
     - ````
   * - ``MAV``
     - ````
   * - ``MI``
     - ````
   * - ``MK``
     - ````
   * - ``MKOND``
     - ````
   * - ``MMAX_INST``
     - ````
   * - ``MMIN_INST``
     - ````
   * - ``MVEC``
     - ````
   * - ``MVECMAX_INST``
     - ````
   * - ``MVECMIN_INST``
     - ````
   * - ``PAV``
     - ````
   * - ``PDAMPF``
     - ````
   * - ``PHR``
     - ````
   * - ``PHVEC``
     - ````
   * - ``PMAX``
     - ````
   * - ``PMIN``
     - ````
   * - ``PR``
     - ````
   * - ``PVEC``
     - ````
   * - ``PVECMAX_INST``
     - ````
   * - ``PVECMIN_INST``
     - ````
   * - ``QI2``
     - ````
   * - ``QK2``
     - ````
   * - ``QMAV``
     - ````
   * - ``QMI``
     - ````
   * - ``QMK``
     - ````
   * - ``QMMAX_INST``
     - ````
   * - ``QMMIN_INST``
     - ````
   * - ``QMVEC``
     - ````
   * - ``QSVB``
     - ````
   * - ``RHOAV``
     - ````
   * - ``RHOI``
     - ````
   * - ``RHOK``
     - ````
   * - ``RHOVEC``
     - ````
   * - ``SVEC``
     - ````
   * - ``TAV``
     - ````
   * - ``TI``
     - ````
   * - ``TK``
     - ``string``
   * - ``TTRVEC``
     - ````
   * - ``TVEC``
     - ````
   * - ``TVECMAX_INST``
     - ````
   * - ``TVECMIN_INST``
     - ````
   * - ``VAV``
     - ````
   * - ``VI``
     - ````
   * - ``VK``
     - ````
   * - ``VMAX_INST``
     - ````
   * - ``VMIN_INST``
     - ````
   * - ``VOLDA``
     - ````
   * - ``WALTERI``
     - ````
   * - ``WALTERK``
     - ````
   * - ``WVL``
     - ````
   * - ``ZAUS``
     - ``single``
   * - ``ZEIN``
     - ``single``
   * - ``ZHKNR``
     - ````
   * - ``ZVEC``
     - ````

PipeGroup
^^^^^^^^^

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

PipeTable
^^^^^^^^^

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

PipeTable_Row
^^^^^^^^^^^^^

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

PipeVertex
^^^^^^^^^^

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
     - Value Type
   * - ``H``
     - ````
   * - ``M``
     - ````
   * - ``MAINELEMENT``
     - ````
   * - ``MMAX_INST``
     - ````
   * - ``MMIN_INST``
     - ````
   * - ``P``
     - ````
   * - ``PH``
     - ````
   * - ``PMAX_INST``
     - ````
   * - ``PMIN_INST``
     - ````
   * - ``RHO``
     - ````
   * - ``T``
     - ````
   * - ``TMAX_INST``
     - ````
   * - ``TMIN_INST``
     - ````

Polygon
^^^^^^^

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

Polyline
^^^^^^^^

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

PressureRegulator
^^^^^^^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ````
   * - ``Beschreibung``
     - ````
   * - ``Dn``
     - ````
   * - ``Typ``
     - ````
   * - ``Indprg``
     - ````
   * - ``Fkzep1``
     - ````
   * - ``Ts``
     - ````
   * - ``Fkcont``
     - ````
   * - ``Idreferenz``
     - ````
   * - ``Iplanung``
     - ````
   * - ``Tk``
     - ````
   * - ``Pk``
     - ````
   * - ``InVariant``
     - ````
   * - ``Xkor``
     - ````
   * - ``Ykor``
     - ````
   * - ``ShowDescription``
     - ````
   * - ``PositionOfDescription``
     - ````
   * - ``Angle``
     - ````
   * - ``SymbolFactor``
     - ````
   * - ``GeometriesDiffer``
     - ````
   * - ``bz.Fk``
     - ````
   * - ``bz.Indsoll``
     - ````
   * - ``bz.Phsoll``
     - ````
   * - ``bz.Fkswvt``
     - ````

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``DH``
     - ````
   * - ``DP``
     - ````
   * - ``DPH``
     - ````
   * - ``DSI``
     - ````
   * - ``DSK``
     - ````
   * - ``FS``
     - ````
   * - ``HR``
     - ````
   * - ``IAKTIV``
     - ````
   * - ``KV``
     - ````
   * - ``M``
     - ````
   * - ``MAINELEMENT``
     - ````
   * - ``PH``
     - ````
   * - ``PHI``
     - ````
   * - ``PHSOLL``
     - ````
   * - ``PR``
     - ````
   * - ``PSOLL``
     - ````
   * - ``QM``
     - ````
   * - ``RHO``
     - ````
   * - ``SWVT``
     - ````
   * - ``V``
     - ````
   * - ``ZETA``
     - ````

PressureZone
^^^^^^^^^^^^

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

Pt1Controller
^^^^^^^^^^^^^

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
     - Value Type
   * - ``MAINELEMENT``
     - ````
   * - ``XA``
     - ````
   * - ``XE``
     - ````

Pump
^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ````
   * - ``Beschreibung``
     - ````
   * - ``Fkpumk``
     - ````
   * - ``Fkpumkturb``
     - ````
   * - ``Qmref``
     - ````
   * - ``Nref``
     - ````
   * - ``Href``
     - ````
   * - ``Pref``
     - ````
   * - ``Qmrefturb``
     - ````
   * - ``Nrefturb``
     - ````
   * - ``Hrefturb``
     - ````
   * - ``Prefturb``
     - ````
   * - ``Nmin``
     - ````
   * - ``Nmax``
     - ````
   * - ``Q0min``
     - ````
   * - ``Q0max``
     - ````
   * - ``Fkkref1``
     - ````
   * - ``Fkkref2``
     - ````
   * - ``Jwirk``
     - ````
   * - ``Traeg``
     - ````
   * - ``Jrlsp``
     - ````
   * - ``Dndtma``
     - ````
   * - ``Indl``
     - ````
   * - ``Fketam``
     - ````
   * - ``Fketau``
     - ````
   * - ``Fketar``
     - ````
   * - ``Nemot``
     - ````
   * - ``Etamot``
     - ````
   * - ``Schlupf``
     - ````
   * - ``Bkfak``
     - ````
   * - ``Tsig``
     - ````
   * - ``Dndt``
     - ````
   * - ``Ntrudel``
     - ````
   * - ``Dngross``
     - ````
   * - ``Dnklein``
     - ````
   * - ``Dt0aus``
     - ````
   * - ``Indasf``
     - ````
   * - ``Wscasf``
     - ````
   * - ``Fkkiasf``
     - ````
   * - ``Totasf``
     - ````
   * - ``Wirasf``
     - ````
   * - ``Indaps``
     - ````
   * - ``Psa``
     - ````
   * - ``Fkkiaps``
     - ````
   * - ``Totaps``
     - ````
   * - ``Indapd``
     - ````
   * - ``Papd``
     - ````
   * - ``Fkkiapd``
     - ````
   * - ``Totapd``
     - ````
   * - ``Fkcont``
     - ````
   * - ``Dt0sch``
     - ````
   * - ``Indds``
     - ````
   * - ``Pdsein``
     - ````
   * - ``Fkkrsspd``
     - ````
   * - ``Kpds``
     - ````
   * - ``Kids``
     - ````
   * - ``Kdds``
     - ````
   * - ``Indss``
     - ````
   * - ``Pssein``
     - ````
   * - ``Fkkrssps``
     - ````
   * - ``Kpss``
     - ````
   * - ``Kiss``
     - ````
   * - ``Kdss``
     - ````
   * - ``Indstf``
     - ````
   * - ``Wscstf``
     - ````
   * - ``Fkkr1stf``
     - ````
   * - ``Wirstf``
     - ````
   * - ``Kpstf``
     - ````
   * - ``Kistf``
     - ````
   * - ``Kdstf``
     - ````
   * - ``Indstd``
     - ````
   * - ``Ifgsw``
     - ````
   * - ``Wsostd``
     - ````
   * - ``Fkkr3std``
     - ````
   * - ``Fkkr4std``
     - ````
   * - ``Wirstd``
     - ````
   * - ``Kpstd``
     - ````
   * - ``Kistd``
     - ````
   * - ``Kdstd``
     - ````
   * - ``Dt0std``
     - ````
   * - ``Idreferenz``
     - ````
   * - ``Iplanung``
     - ````
   * - ``PerformanceMapParameters``
     - ````
   * - ``BKFaktTubine``
     - ````
   * - ``EtaRef``
     - ````
   * - ``EtaRefTurb``
     - ````
   * - ``IndLTurb``
     - ````
   * - ``NMaxTurb``
     - ````
   * - ``NMinTurb``
     - ````
   * - ``Q0MaxTurb``
     - ````
   * - ``Q0MinTurb``
     - ````
   * - ``PukfString``
     - ````
   * - ``Tk``
     - ````
   * - ``Pk``
     - ````
   * - ``InVariant``
     - ````
   * - ``Xkor``
     - ````
   * - ``Ykor``
     - ````
   * - ``ShowDescription``
     - ````
   * - ``PositionOfDescription``
     - ````
   * - ``Angle``
     - ````
   * - ``SymbolFactor``
     - ````
   * - ``GeometriesDiffer``
     - ````
   * - ``bz.Fk``
     - ````
   * - ``bz.Inds``
     - ````
   * - ``bz.Indturb``
     - ````
   * - ``bz.Ispu``
     - ````
   * - ``bz.Isputurb``
     - ````
   * - ``bz.Qmsoll``
     - ````
   * - ``bz.Nsoll``
     - ````
   * - ``bz.Qmsollturb``
     - ````
   * - ``bz.Nsollturb``
     - ````
   * - ``bz.Phsoll``
     - ````
   * - ``bz.Fkrcpl``
     - ````
   * - ``bz.Inda``
     - ````
   * - ``bz.Tipu``
     - ````
   * - ``bz.Fkpumd``
     - ````
   * - ``bz.Fkswvt``
     - ````
   * - ``bz.IndATurb``
     - ````
   * - ``bz.IndSTurb``
     - ````
   * - ``bz.IndsKlartext``
     - ````
   * - ``bz.IndaKlartext``
     - ````
   * - ``bz.IspuKlartext``
     - ````

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``BK``
     - ````
   * - ``DH``
     - ````
   * - ``DP``
     - ````
   * - ``DPH``
     - ````
   * - ``EINAUS``
     - ````
   * - ``ETA``
     - ````
   * - ``ETAW``
     - ````
   * - ``IAKTIV``
     - ````
   * - ``IND``
     - ````
   * - ``M``
     - ````
   * - ``MAINELEMENT``
     - ````
   * - ``MOM``
     - ````
   * - ``N``
     - ````
   * - ``NMINMAXDIF``
     - ````
   * - ``NPSH``
     - ````
   * - ``NPSHDIF``
     - ````
   * - ``NPSHMIN``
     - ````
   * - ``NSOLLTURB``
     - ````
   * - ``PA``
     - ````
   * - ``PE``
     - ````
   * - ``PE_RUECK``
     - ````
   * - ``PHSOLL``
     - ````
   * - ``PP``
     - ````
   * - ``PUMD``
     - ````
   * - ``QM``
     - ````
   * - ``QMSOLL``
     - ````
   * - ``QMSOLLTURB``
     - ````
   * - ``QN0``
     - ````
   * - ``RCPU_IND``
     - ````
   * - ``RCPU_W``
     - ````
   * - ``RCPU_X``
     - ````
   * - ``RCPU_XD``
     - ````
   * - ``RHO``
     - ````
   * - ``STOERUNG``
     - ````
   * - ``SWVT``
     - ````

PumpCharTable
^^^^^^^^^^^^^

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

PumpCharTable_Row
^^^^^^^^^^^^^^^^^

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

PumpGroup
^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ````
   * - ``Beschreibung``
     - ````
   * - ``Ibyp``
     - ````
   * - ``ActAsa``
     - ````
   * - ``AusAsa``
     - ````
   * - ``Fkkibyp``
     - ````
   * - ``Fkkkbyp``
     - ````
   * - ``Ischalt``
     - ````
   * - ``Qmaus``
     - ````
   * - ``Dphaus``
     - ````
   * - ``Indrst``
     - ````
   * - ``Nmax``
     - ````
   * - ``Pdmax``
     - ````
   * - ``Fkkdmax``
     - ````
   * - ``Psmin``
     - ````
   * - ``Fkksmin``
     - ````
   * - ``Fkcont``
     - ````
   * - ``Idreferenz``
     - ````
   * - ``Iplanung``
     - ````
   * - ``Tk``
     - ````
   * - ``Pk``
     - ````
   * - ``InVariant``
     - ````
   * - ``Xkor``
     - ````
   * - ``Ykor``
     - ````
   * - ``BoundingRectangle``
     - ````
   * - ``bz.Fk``
     - ````
   * - ``bz.Iaktiv``
     - ````
   * - ``bz.Indpg``
     - ````
   * - ``bz.Fkrart``
     - ````

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``BK``
     - ````
   * - ``DH``
     - ````
   * - ``DP``
     - ````
   * - ``DPH``
     - ````
   * - ``ETA``
     - ````
   * - ``IAKTIV``
     - ````
   * - ``INDPG``
     - ````
   * - ``INDSTD``
     - ````
   * - ``IZSTPG``
     - ````
   * - ``M``
     - ````
   * - ``MAINELEMENT``
     - ````
   * - ``NPUMPIST``
     - ````
   * - ``NPUMPSOLL``
     - ````
   * - ``PE``
     - ````
   * - ``QM``
     - ````
   * - ``RART``
     - ````
   * - ``RHO``
     - ````
   * - ``W``
     - ````
   * - ``X``
     - ````

PumpOfPumpGroup
^^^^^^^^^^^^^^^

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
     - Value Type
   * - ``IAKTIV``
     - ````
   * - ``MAINELEMENT``
     - ````

PumpSpeedTable
^^^^^^^^^^^^^^

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
     - Value Type
   * - ``MAINELEMENT``
     - ````
   * - ``N``
     - ````

PumpSpeedTable_Row
^^^^^^^^^^^^^^^^^^

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

RART_ControlMode
^^^^^^^^^^^^^^^^

Properties
""""""""""

No properties found.

Result Properties
"""""""""""""""""

No result properties found.

REGP_ControlParameters
^^^^^^^^^^^^^^^^^^^^^^

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

RMES_DPTS_RmesInternalDataPoint
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

Rectangle
^^^^^^^^^

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

RegulatorsTable
^^^^^^^^^^^^^^^

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

RegulatorsTable_Row
^^^^^^^^^^^^^^^^^^^

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

ReturnTemperaturTable
^^^^^^^^^^^^^^^^^^^^^

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

ReturnTemperaturTable_Row
^^^^^^^^^^^^^^^^^^^^^^^^^

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

RoundRectangle
^^^^^^^^^^^^^^

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

SIRGRAF
^^^^^^^

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

SPLZ_TimeSeries
^^^^^^^^^^^^^^^

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

SafetyValve
^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ````
   * - ``Beschreibung``
     - ````
   * - ``Dn``
     - ````
   * - ``Typ``
     - ````
   * - ``Fkkref``
     - ````
   * - ``Fkzep2``
     - ````
   * - ``Fkphi2``
     - ````
   * - ``Fkcont``
     - ````
   * - ``Idreferenz``
     - ````
   * - ``Iplanung``
     - ````
   * - ``Tk``
     - ````
   * - ``Pk``
     - ````
   * - ``InVariant``
     - ````
   * - ``Xkor``
     - ````
   * - ``Ykor``
     - ````
   * - ``ShowDescription``
     - ````
   * - ``PositionOfDescription``
     - ````
   * - ``Angle``
     - ````
   * - ``SymbolFactor``
     - ````
   * - ``GeometriesDiffer``
     - ````
   * - ``bz.Fk``
     - ````
   * - ``bz.Phis``
     - ````
   * - ``bz.Psch``
     - ````

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``DH``
     - ````
   * - ``DP``
     - ````
   * - ``DPH``
     - ````
   * - ``DSI``
     - ````
   * - ``DSK``
     - ````
   * - ``FS``
     - ````
   * - ``HR``
     - ````
   * - ``IAKTIV``
     - ````
   * - ``M``
     - ````
   * - ``MAINELEMENT``
     - ````
   * - ``PHI``
     - ````
   * - ``PHSCH``
     - ````
   * - ``PR``
     - ````
   * - ``QM``
     - ````
   * - ``RHO``
     - ````
   * - ``V``
     - ````
   * - ``ZETA``
     - ````

SetpointDevice
^^^^^^^^^^^^^^

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
     - Value Type
   * - ``LFKT``
     - ````
   * - ``MAINELEMENT``
     - ````
   * - ``SLWKON``
     - ````
   * - ``SWVT``
     - ````
   * - ``W``
     - ````
   * - ``WAKT``
     - ````
   * - ``WE``
     - ````
   * - ``WEAKT``
     - ````
   * - ``WERCK``
     - ````
   * - ``WRCK``
     - ````
   * - ``XA``
     - ````

SolarCollector
^^^^^^^^^^^^^^

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

StandPipe
^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ````
   * - ``Beschreibung``
     - ````
   * - ``Indatab``
     - ````
   * - ``A``
     - ````
   * - ``Hb``
     - ````
   * - ``U``
     - ````
   * - ``Mue``
     - ````
   * - ``Fkatab``
     - ````
   * - ``Dn``
     - ````
   * - ``Zetapos``
     - ````
   * - ``Zetaneg``
     - ````
   * - ``Knotk``
     - ````
   * - ``Zkor``
     - ````
   * - ``Fkfstf``
     - ````
   * - ``Fkcont``
     - ````
   * - ``Idreferenz``
     - ````
   * - ``Iplanung``
     - ````
   * - ``Tk``
     - ````
   * - ``Pk``
     - ````
   * - ``InVariant``
     - ````
   * - ``GeometriesDiffer``
     - ````
   * - ``SymbolGraf``
     - ````
   * - ``SymbolFactor``
     - ````
   * - ``Xkor``
     - ````
   * - ``Ykor``
     - ````
   * - ``Angle``
     - ````
   * - ``bz.Fk``
     - ````

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``IAKTIV``
     - ````
   * - ``M``
     - ````
   * - ``MAINELEMENT``
     - ````
   * - ``MUEB``
     - ````
   * - ``QM``
     - ````
   * - ``QMUEB``
     - ````
   * - ``RHO``
     - ````
   * - ``T``
     - ````
   * - ``V``
     - ````
   * - ``VOL``
     - ````
   * - ``WALTER``
     - ````
   * - ``WST``
     - ````

Street
^^^^^^

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

SummingPoint
^^^^^^^^^^^^

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
     - Value Type
   * - ``MAINELEMENT``
     - ````
   * - ``XA``
     - ````
   * - ``XE1``
     - ````
   * - ``XE2``
     - ````

SwitchInBlock
^^^^^^^^^^^^^

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

TemperatureTable
^^^^^^^^^^^^^^^^

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
     - Value Type
   * - ``MAINELEMENT``
     - ````
   * - ``T``
     - ````

TemperatureTable_Row
^^^^^^^^^^^^^^^^^^^^

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

Text
^^^^

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

ThermalOutputTable
^^^^^^^^^^^^^^^^^^

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
     - Value Type
   * - ``MAINELEMENT``
     - ````
   * - ``W``
     - ````

ThermalOutputTable_Row
^^^^^^^^^^^^^^^^^^^^^^

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

ThermophysPropTable
^^^^^^^^^^^^^^^^^^^

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

ThermophysPropTable_Row
^^^^^^^^^^^^^^^^^^^^^^^

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

TransitionSymbol
^^^^^^^^^^^^^^^^

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

Transmitter
^^^^^^^^^^^

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
     - Value Type
   * - ``MAINELEMENT``
     - ````
   * - ``XA``
     - ````
   * - ``XM``
     - ````
   * - ``XU``
     - ````

TransportVariable
^^^^^^^^^^^^^^^^^

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

USCH_UserDefinedProperties
^^^^^^^^^^^^^^^^^^^^^^^^^^

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

Unknown
^^^^^^^

Properties
""""""""""

No properties found.

Result Properties
"""""""""""""""""

No result properties found.

VARA_ColorScale
^^^^^^^^^^^^^^^

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

VARA_ROWS_WidthOrScale
^^^^^^^^^^^^^^^^^^^^^^

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

VRCT_ViewRectangle
^^^^^^^^^^^^^^^^^^

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

Valve
^^^^^

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
     - Value Type
   * - ``AUF``
     - ````
   * - ``AUFZU``
     - ````
   * - ``DH``
     - ````
   * - ``DP``
     - ````
   * - ``DSI``
     - ````
   * - ``DSK``
     - ````
   * - ``FREIGABE``
     - ````
   * - ``FS``
     - ````
   * - ``HR``
     - ````
   * - ``IAKTIV``
     - ````
   * - ``KV``
     - ````
   * - ``LAEUFT``
     - ````
   * - ``M``
     - ````
   * - ``MAINELEMENT``
     - ````
   * - ``OEFFNET``
     - ````
   * - ``PHI``
     - ````
   * - ``PHI1``
     - ````
   * - ``PHR``
     - ````
   * - ``PR``
     - ````
   * - ``Q2``
     - ````
   * - ``QM``
     - ````
   * - ``RHO``
     - ````
   * - ``SCHLIESST``
     - ````
   * - ``STOERUNG``
     - ````
   * - ``V``
     - ````
   * - ``ZETA``
     - ````
   * - ``ZU``
     - ````

ValveLiftTable
^^^^^^^^^^^^^^

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
     - Value Type
   * - ``MAINELEMENT``
     - ````
   * - ``PHI``
     - ````

ValveLiftTable_Row
^^^^^^^^^^^^^^^^^^

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

VarFlowTable
^^^^^^^^^^^^

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
     - Value Type
   * - ``FWVB_DPHMIN``
     - ````
   * - ``FWVB_TVLMIN``
     - ````
   * - ``MAINELEMENT``
     - ````
   * - ``MFVHYUV``
     - ````
   * - ``MFVTHUV``
     - ````
   * - ``NFVHYUV``
     - ````
   * - ``NFVTHUV``
     - ````
   * - ``QM``
     - ````
   * - ``TVMINMAX``
     - ````

VarFlowTable_Row
^^^^^^^^^^^^^^^^

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

VarPressureTable
^^^^^^^^^^^^^^^^

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
     - Value Type
   * - ``MAINELEMENT``
     - ````
   * - ``PH``
     - ````

VarPressureTable_Row
^^^^^^^^^^^^^^^^^^^^

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

VentOpenCloseTable
^^^^^^^^^^^^^^^^^^

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

VentOpenCloseTable_Row
^^^^^^^^^^^^^^^^^^^^^^

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

VentValve
^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ````
   * - ``Beschreibung``
     - ````
   * - ``Dgr``
     - ````
   * - ``Dkl``
     - ````
   * - ``Alpha``
     - ````
   * - ``Vgrest``
     - ````
   * - ``Qlbmax``
     - ````
   * - ``Qlekl``
     - ````
   * - ``Rgbeve``
     - ````
   * - ``Trohr``
     - ````
   * - ``Poeff``
     - ````
   * - ``Ibedef``
     - ````
   * - ``Ibetyp``
     - ````
   * - ``Knotk``
     - ````
   * - ``Zkor``
     - ````
   * - ``Fkfstf``
     - ````
   * - ``Iekl``
     - ````
   * - ``Fkcont``
     - ````
   * - ``Idreferenz``
     - ````
   * - ``Iplanung``
     - ````
   * - ``Tk``
     - ````
   * - ``Pk``
     - ````
   * - ``InVariant``
     - ````
   * - ``GeometriesDiffer``
     - ````
   * - ``SymbolGraf``
     - ````
   * - ``SymbolFactor``
     - ````
   * - ``Xkor``
     - ````
   * - ``Ykor``
     - ````
   * - ``Angle``
     - ````
   * - ``bz.Fk``
     - ````

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``IAKTIV``
     - ````
   * - ``IND``
     - ````
   * - ``M``
     - ````
   * - ``MAINELEMENT``
     - ````
   * - ``MLUFT``
     - ````
   * - ``PHI``
     - ````
   * - ``PLUFT``
     - ````
   * - ``QLUFT``
     - ````
   * - ``QM``
     - ````
   * - ``QMLUFT``
     - ````
   * - ``RHO``
     - ````
   * - ``TLUFT``
     - ````
   * - ``VLUFT``
     - ````
   * - ``VOLLUFT``
     - ````

VentilatedPressureAirVessel
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``Name``
     - ````
   * - ``Beschreibung``
     - ````
   * - ``Indatab``
     - ````
   * - ``A``
     - ````
   * - ``Lta``
     - ````
   * - ``Hb``
     - ````
   * - ``Pg0``
     - ````
   * - ``Tgas``
     - ````
   * - ``Fkatab``
     - ````
   * - ``Dn``
     - ````
   * - ``Zetapos``
     - ````
   * - ``Zetaneg``
     - ````
   * - ``Rgas``
     - ````
   * - ``Rpoly``
     - ````
   * - ``Knotk``
     - ````
   * - ``Zkor``
     - ````
   * - ``Fkfstf``
     - ````
   * - ``Fkcont``
     - ````
   * - ``Idreferenz``
     - ````
   * - ``Iplanung``
     - ````
   * - ``Tk``
     - ````
   * - ``Pk``
     - ````
   * - ``InVariant``
     - ````
   * - ``GeometriesDiffer``
     - ````
   * - ``SymbolGraf``
     - ````
   * - ``SymbolFactor``
     - ````
   * - ``Xkor``
     - ````
   * - ``Ykor``
     - ````
   * - ``Angle``
     - ````
   * - ``bz.Fk``
     - ````

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Type
   * - ``HLUFT``
     - ````
   * - ``IAKTIV``
     - ````
   * - ``IND``
     - ````
   * - ``M``
     - ````
   * - ``MAINELEMENT``
     - ````
   * - ``PLUFT``
     - ````
   * - ``QM``
     - ````
   * - ``RHO``
     - ````
   * - ``T``
     - ````
   * - ``TLUFT``
     - ````
   * - ``V``
     - ````
   * - ``VOL``
     - ````
   * - ``VOLLUFT``
     - ````
   * - ``VOLLUFT1``
     - ````
   * - ``WALTER``
     - ````
   * - ``WST``
     - ````

WBLZ_ThermalBalance
^^^^^^^^^^^^^^^^^^^

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
     - Value Type
   * - ``MAINELEMENT``
     - ````
   * - ``WES``
     - ````
   * - ``WRAND``
     - ````
   * - ``WSPEI``
     - ````
   * - ``WSPEI_SP``
     - ````
   * - ``WVB``
     - ````
   * - ``WVB_0``
     - ````
   * - ``WVB_W``
     - ````
   * - ``WVB_XD``
     - ````
   * - ``WVERL``
     - ````
   * - ``WWU``
     - ````

WeatherDataTable
^^^^^^^^^^^^^^^^

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
     - Value Type
   * - ``GDIFF``
     - ````
   * - ``GGLOB``
     - ````
   * - ``MAINELEMENT``
     - ````
   * - ``TEMP``
     - ````
   * - ``WIND``
     - ````

WeatherDataTable_Row
^^^^^^^^^^^^^^^^^^^^

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

