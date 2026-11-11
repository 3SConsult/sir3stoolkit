Object Types, Properties, and Result Value Types
---------------------------------------------

.. note:: Aggregated global view across configured network types.
   The below sections lists all table names from self.ObjectTypes_TableNames, along with their properties, result properties, and respective object type from self.ObjectTypes (needed for toolkit operations like self.InsertElement(), self.GetPropertiesOfElementType()).
   Result properties are listed by name only.

AGSN_HydraulicProfile
^^^^^^^^^^^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``Aktiv``
     - ``int32``
   * - ``AllNodesAndLinks``
     - ``dictionary`2``
   * - ``InVariant``
     - ``boolean``
   * - ``Lfdnr``
     - ``int32``
   * - ``MainWay``
     - ``iagsnway``
   * - ``Name``
     - ``string``
   * - ``ObjsString``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Tk``
     - ``string``

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
     - Value Types
   * - ``A``
     - ``single``
   * - ``Angle``
     - ``double``
   * - ``Beschreibung``
     - ``string``
   * - ``Dn``
     - ``single``
   * - ``Fkatab``
     - ``string``
   * - ``Fkcont``
     - ``string``
   * - ``Fkfstf``
     - ``string``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``Hb``
     - ``single``
   * - ``Ibla``
     - ``int32``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Indatab``
     - ``int32``
   * - ``Iplanung``
     - ``int32``
   * - ``Knotk``
     - ``string``
   * - ``Name``
     - ``string``
   * - ``Pg0``
     - ``single``
   * - ``Pk``
     - ``string``
   * - ``Rgas``
     - ``single``
   * - ``Rpoly``
     - ``single``
   * - ``SymbolFactor``
     - ``double``
   * - ``SymbolGraf``
     - ``symbol1c_graf``
   * - ``Tgas``
     - ``single``
   * - ``Tk``
     - ``string``
   * - ``Vg0``
     - ``single``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``Zetaneg``
     - ``single``
   * - ``Zetapos``
     - ``single``
   * - ``Zkor``
     - ``single``
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

Arrow
^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``Angle``
     - ``double``
   * - ``Beschreibung``
     - ``string``
   * - ``Fkcont``
     - ``string``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``SymbolFactor``
     - ``double``
   * - ``Tk``
     - ``string``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
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
     - Value Types
   * - ``InVariant``
     - ``boolean``
   * - ``Indbarf``
     - ``int32``
   * - ``Name``
     - ``string``
   * - ``Patmos``
     - ``single``
   * - ``Pk``
     - ``string``
   * - ``Rgas``
     - ``single``
   * - ``Rpoly``
     - ``single``
   * - ``Tatmos``
     - ``single``

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
     - Value Types
   * - ``Displaymode``
     - ``int32``
   * - ``Fkcont``
     - ``string``
   * - ``Fkknot``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Pointinsertx``
     - ``double``
   * - ``Pointinserty``
     - ``double``
   * - ``Posname``
     - ``int32``
   * - ``Showname``
     - ``int32``
   * - ``Symbolfact``
     - ``single``

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
     - Value Types
   * - ``InVariant``
     - ``boolean``
   * - ``Name``
     - ``string``
   * - ``Nglopt``
     - ``int32``
   * - ``Pk``
     - ``string``
   * - ``bz.Epsp``
     - ``single``
   * - ``bz.Epspreg``
     - ``single``
   * - ``bz.Epsqm``
     - ``single``
   * - ``bz.Epsqmreg``
     - ``single``
   * - ``bz.Epst``
     - ``single``
   * - ``bz.Epstrsp``
     - ``single``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.Ntiter``
     - ``int32``
   * - ``bz.Ntrspiter``
     - ``int32``
   * - ``bz.Nziter``
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
     - Value Types
   * - ``Beschreibung``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Kvbzg``
     - ``single``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Typ``
     - ``int32``
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
     - Value Types
   * - ``Fk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Kvrelneg``
     - ``single``
   * - ``Kvrelpos``
     - ``single``
   * - ``Name``
     - ``string``
   * - ``Phi``
     - ``single``
   * - ``Pk``
     - ``string``
   * - ``Zetaneg``
     - ``single``
   * - ``Zetapos``
     - ``single``

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
     - Value Types
   * - ``Beschreibung``
     - ``string``
   * - ``FillColor``
     - ``color``
   * - ``Fkcont``
     - ``string``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``LineColor``
     - ``color``
   * - ``LineWidthMM``
     - ``double``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Tk``
     - ``string``
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
     - Value Types
   * - ``Angle``
     - ``double``
   * - ``Beschreibung``
     - ``string``
   * - ``Dndt``
     - ``single``
   * - ``Dpdt``
     - ``single``
   * - ``Dqndt``
     - ``single``
   * - ``Etam``
     - ``single``
   * - ``Etat``
     - ``single``
   * - ``Fkantp``
     - ``string``
   * - ``Fkcont``
     - ``string``
   * - ``Fkkomk``
     - ``string``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``Ibrenng``
     - ``int32``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Inda``
     - ``int32``
   * - ``Iplanung``
     - ``int32``
   * - ``Iprst``
     - ``int32``
   * - ``Ipverh``
     - ``int32``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``PositionOfDescription``
     - ``int32``
   * - ``Pverhdp``
     - ``single``
   * - ``Pverhqn``
     - ``single``
   * - ``ShowDescription``
     - ``boolean``
   * - ``SymbolFactor``
     - ``double``
   * - ``Tfahraus``
     - ``single``
   * - ``Tfahrein``
     - ``single``
   * - ``Tk``
     - ``string``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
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

CompressorTable
^^^^^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``Beschreibung``
     - ``string``
   * - ``Etaps``
     - ``single``
   * - ``Fkfstf``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Name``
     - ``string``
   * - ``Nmax``
     - ``single``
   * - ``Nmin``
     - ``single``
   * - ``Pansaug``
     - ``single``
   * - ``Pk``
     - ``string``
   * - ``Tansaug``
     - ``single``
   * - ``Tk``
     - ``string``
   * - ``Typ``
     - ``int32``
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
     - Value Types
   * - ``Etap``
     - ``single``
   * - ``Fk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``N``
     - ``single``
   * - ``Name``
     - ``string``
   * - ``P``
     - ``single``
   * - ``Pk``
     - ``string``
   * - ``Q``
     - ``single``
   * - ``Yp``
     - ``single``

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
     - Value Types
   * - ``Fkcont``
     - ``string``
   * - ``Idxke``
     - ``int32``
   * - ``InVariant``
     - ``boolean``
   * - ``LineWidthMM``
     - ``double``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Tk``
     - ``string``

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
     - Value Types
   * - ``Beschreibung``
     - ``string``
   * - ``Dwdt``
     - ``single``
   * - ``Fkkref1``
     - ``string``
   * - ``Fkkref2``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Indstd``
     - ``int32``
   * - ``Lfdnr``
     - ``int32``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Tsig``
     - ``single``
   * - ``TypeDescription``
     - ``string``
   * - ``Xdein``
     - ``single``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.Fkrcpl``
     - ``string``
   * - ``bz.Fkswvt``
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

ControlPointTable
^^^^^^^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``Aktiv``
     - ``int32``
   * - ``Beschreibung``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Typ``
     - ``int32``

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

ControlPointTable_Row
^^^^^^^^^^^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``Aktiv``
     - ``int32``
   * - ``Fk``
     - ``string``
   * - ``Fkkref1``
     - ``string``
   * - ``Fkkref2``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``W``
     - ``single``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``MAINELEMENT``
   * - ``W``
   * - ``X``
   * - ``XD``

ControlValve
^^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``Angle``
     - ``double``
   * - ``Beschreibung``
     - ``string``
   * - ``Dn``
     - ``single``
   * - ``Fkcont``
     - ``string``
   * - ``Fkzep1``
     - ``string``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Iplanung``
     - ``int32``
   * - ``Name``
     - ``string``
   * - ``OnlStrgString``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``PositionOfDescription``
     - ``int32``
   * - ``ShowDescription``
     - ``boolean``
   * - ``SymbolFactor``
     - ``double``
   * - ``Thub``
     - ``single``
   * - ``Tk``
     - ``string``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
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

ControlVariableConverter
^^^^^^^^^^^^^^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``AnalogInputE1``
     - ``string``
   * - ``Angle``
     - ``double``
   * - ``Beschreibung``
     - ``string``
   * - ``Dsdt``
     - ``single``
   * - ``Fkcont``
     - ``string``
   * - ``Fkdprg``
     - ``string``
   * - ``Fkfwes``
     - ``string``
   * - ``Fkfwwu``
     - ``string``
   * - ``Fkgvwk``
     - ``string``
   * - ``Fkknot``
     - ``string``
   * - ``Fkkomp``
     - ``string``
   * - ``Fkmreg``
     - ``string``
   * - ``Fkobeh``
     - ``string``
   * - ``Fkpgrp``
     - ``string``
   * - ``Fkpreg``
     - ``string``
   * - ``Fkpump``
     - ``string``
   * - ``Fkpumppg``
     - ``string``
   * - ``Fkrart``
     - ``string``
   * - ``Fkrartpg``
     - ``string``
   * - ``Fkregv``
     - ``string``
   * - ``Fkrohr``
     - ``string``
   * - ``Fkvent``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Indyno``
     - ``int32``
   * - ``Ityp``
     - ``int32``
   * - ``Ka``
     - ``string``
   * - ``LogicalInputE2``
     - ``string``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``RglSymbolTyp``
     - ``rglsymboltype``
   * - ``SymbolFactor``
     - ``double``
   * - ``Tk``
     - ``string``
   * - ``Typ``
     - ``string``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``Ymax``
     - ``single``
   * - ``Ymin``
     - ``single``
   * - ``Ys1``
     - ``single``
   * - ``Ys2``
     - ``single``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.Fklfkt``
     - ``string``
   * - ``bz.Fkphi1``
     - ``string``
   * - ``bz.Fkpumd``
     - ``string``
   * - ``bz.Fkpvar``
     - ``string``
   * - ``bz.Fkqvar``
     - ``string``
   * - ``bz.Fkrcpl``
     - ``string``
   * - ``bz.FkrcplRowt``
     - ``string``
   * - ``bz.Fkswvt``
     - ``string``
   * - ``bz.Fktevt``
     - ``string``
   * - ``bz.Fkwevt``
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

ControlVariableConverterRSTE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``Angle``
     - ``double``
   * - ``Beschreibung``
     - ``string``
   * - ``Dsdt1``
     - ``single``
   * - ``Dsdt2``
     - ``single``
   * - ``Dsdt3``
     - ``single``
   * - ``Dsdt4``
     - ``single``
   * - ``Dsdt5``
     - ``single``
   * - ``Fkcont``
     - ``string``
   * - ``Fkvbel1``
     - ``string``
   * - ``Fkvbel2``
     - ``string``
   * - ``Fkvbel3``
     - ``string``
   * - ``Fkvbel4``
     - ``string``
   * - ``Fkvbel5``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Indyno1``
     - ``int32``
   * - ``Indyno2``
     - ``int32``
   * - ``Indyno3``
     - ``int32``
   * - ``Indyno4``
     - ``int32``
   * - ``Indyno5``
     - ``int32``
   * - ``Ka``
     - ``string``
   * - ``Kmes1i``
     - ``string``
   * - ``Kmes1k``
     - ``string``
   * - ``Kmes2i``
     - ``string``
   * - ``Kmes2k``
     - ``string``
   * - ``Kmes3i``
     - ``string``
   * - ``Kmes3k``
     - ``string``
   * - ``Kmes4i``
     - ``string``
   * - ``Kmes4k``
     - ``string``
   * - ``Kmes5i``
     - ``string``
   * - ``Kmes5k``
     - ``string``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``RglSymbolTyp``
     - ``rglsymboltype``
   * - ``SymbolFactor``
     - ``double``
   * - ``Tk``
     - ``string``
   * - ``Typ1``
     - ``string``
   * - ``Typ2``
     - ``string``
   * - ``Typ3``
     - ``string``
   * - ``Typ4``
     - ``string``
   * - ``Typ5``
     - ``string``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``Ymax1``
     - ``single``
   * - ``Ymax2``
     - ``single``
   * - ``Ymax3``
     - ``single``
   * - ``Ymax4``
     - ``single``
   * - ``Ymax5``
     - ``single``
   * - ``Ymin1``
     - ``single``
   * - ``Ymin2``
     - ``single``
   * - ``Ymin3``
     - ``single``
   * - ``Ymin4``
     - ``single``
   * - ``Ymin5``
     - ``single``
   * - ``Ys11``
     - ``single``
   * - ``Ys12``
     - ``single``
   * - ``Ys13``
     - ``single``
   * - ``Ys14``
     - ``single``
   * - ``Ys15``
     - ``single``
   * - ``Ys21``
     - ``single``
   * - ``Ys22``
     - ``single``
   * - ``Ys23``
     - ``single``
   * - ``Ys24``
     - ``single``
   * - ``Ys25``
     - ``single``
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

CrossSectionTable
^^^^^^^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``Beschreibung``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Tk``
     - ``string``
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
     - Value Types
   * - ``Fk``
     - ``string``
   * - ``Flaeche``
     - ``single``
   * - ``InVariant``
     - ``boolean``
   * - ``Name``
     - ``string``
   * - ``Ordinate``
     - ``single``
   * - ``Pk``
     - ``string``

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
     - Value Types
   * - ``Fkdpgr``
     - ``string``
   * - ``Fkdpkt``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Tk``
     - ``string``

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
     - Value Types
   * - ``Description``
     - ``string``
   * - ``Dtfak``
     - ``int32``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Name``
     - ``string``
   * - ``OpcgroupName``
     - ``string``
   * - ``OpcserverPath``
     - ``string``
   * - ``PermissionFlags``
     - ``int32``
   * - ``Pk``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Typ``
     - ``int32``
   * - ``bz.ExternalUse``
     - ``int32``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.LocalUse``
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
     - Value Types
   * - ``Addend``
     - ``single``
   * - ``Attrtype``
     - ``string``
   * - ``ClientFlags``
     - ``int32``
   * - ``ClientId``
     - ``string``
   * - ``Datalength``
     - ``int32``
   * - ``Datatype``
     - ``string``
   * - ``Description``
     - ``string``
   * - ``Deviation``
     - ``single``
   * - ``Epkz``
     - ``int32``
   * - ``Factor``
     - ``single``
   * - ``Fkobjtype``
     - ``string``
   * - ``Flags``
     - ``int32``
   * - ``InVariant``
     - ``boolean``
   * - ``LowerLimit``
     - ``single``
   * - ``Name``
     - ``string``
   * - ``Name1``
     - ``string``
   * - ``Name2``
     - ``string``
   * - ``Name3``
     - ``string``
   * - ``Objtype``
     - ``string``
   * - ``Ol3command``
     - ``string``
   * - ``OpcitemId``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Title``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Unit``
     - ``string``
   * - ``UpperLimit``
     - ``single``
   * - ``bz.Addend``
     - ``single``
   * - ``bz.CheckAbs``
     - ``int32``
   * - ``bz.CheckAll``
     - ``int32``
   * - ``bz.CheckMsg``
     - ``int32``
   * - ``bz.ClientFlags``
     - ``int32``
   * - ``bz.ClientId``
     - ``string``
   * - ``bz.Deviation``
     - ``single``
   * - ``bz.Factor``
     - ``single``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.Fkobjtype``
     - ``string``
   * - ``bz.LimitToler``
     - ``single``
   * - ``bz.LowerLimit``
     - ``single``
   * - ``bz.Name1``
     - ``string``
   * - ``bz.Name2``
     - ``string``
   * - ``bz.Name3``
     - ``string``
   * - ``bz.OpcitemId``
     - ``string``
   * - ``bz.UpperLimit``
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
     - Value Types
   * - ``Beschreibung``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Tk``
     - ``string``
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
     - Value Types
   * - ``Erate``
     - ``single``
   * - ``Fk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Ralter``
     - ``int32``
   * - ``Srate``
     - ``single``

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
     - Value Types
   * - ``Angle``
     - ``double``
   * - ``Beschreibung``
     - ``string``
   * - ``E1``
     - ``string``
   * - ``Fkcont``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Ka``
     - ``string``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``RglSymbolTyp``
     - ``rglsymboltype``
   * - ``SymbolFactor``
     - ``double``
   * - ``Tk``
     - ``string``
   * - ``Ttot``
     - ``single``
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

Demand
^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``AenderungArt``
     - ``int32``
   * - ``AenderungDatum``
     - ``string``
   * - ``AenderungInfo``
     - ``string``
   * - ``Betriebsstatus``
     - ``int32``
   * - ``Betriebsstunden``
     - ``single``
   * - ``Dimension``
     - ``string``
   * - ``ErzeugungArt``
     - ``int32``
   * - ``ErzeugungInfo``
     - ``string``
   * - ``Fkhaus``
     - ``string``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``Graphics``
     - ``hausverbgraf``
   * - ``Hausanlagenbauart``
     - ``string``
   * - ``Hausanlagentyp``
     - ``string``
   * - ``Hausnr``
     - ``int32``
   * - ``HausnrZus``
     - ``string``
   * - ``Heizleistung``
     - ``single``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Jahresarbeit``
     - ``single``
   * - ``Kuehlleistung``
     - ``single``
   * - ``KundenId``
     - ``string``
   * - ``Kundengruppe``
     - ``string``
   * - ``LaengeHal``
     - ``single``
   * - ``LaengeHauseinfuehrung``
     - ``single``
   * - ``MengenbegrHwd``
     - ``single``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Plz``
     - ``int32``
   * - ``Prl``
     - ``single``
   * - ``Pvl``
     - ``single``
   * - ``Qhm``
     - ``single``
   * - ``QhmaxFd``
     - ``single``
   * - ``QhmaxFh``
     - ``single``
   * - ``Rau``
     - ``single``
   * - ``Sonstige``
     - ``single``
   * - ``Spartentyp``
     - ``string``
   * - ``Tariftyp``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Trs0``
     - ``single``
   * - ``Tvl0``
     - ``single``
   * - ``Verbrauch``
     - ``double``
   * - ``VerbrauchDatum``
     - ``string``
   * - ``ViewX``
     - ``double``
   * - ``ViewY``
     - ``double``
   * - ``Warmwasserleistung``
     - ``single``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``ZaehlerId``
     - ``string``
   * - ``Zeta``
     - ``single``
   * - ``Zkor``
     - ``single``
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
     - Value Types
   * - ``Angle``
     - ``double``
   * - ``Beschreibung``
     - ``string``
   * - ``Dn``
     - ``single``
   * - ``Fkcont``
     - ``string``
   * - ``Fkkref1``
     - ``string``
   * - ``Fkkref2``
     - ``string``
   * - ``Fkzep1``
     - ``string``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Iplanung``
     - ``int32``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``PositionOfDescription``
     - ``int32``
   * - ``ShowDescription``
     - ``boolean``
   * - ``SymbolFactor``
     - ``double``
   * - ``Tk``
     - ``string``
   * - ``Ts``
     - ``single``
   * - ``Typ``
     - ``int32``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``bz.Dphsoll``
     - ``single``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.Fkswvt``
     - ``string``
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

DirectionalArrow
^^^^^^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``Angle``
     - ``double``
   * - ``Beschreibung``
     - ``string``
   * - ``FillColor``
     - ``color``
   * - ``Fkcont``
     - ``string``
   * - ``FkdpgrDpkt``
     - ``string``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``InVariant``
     - ``boolean``
   * - ``Inddir``
     - ``int32``
   * - ``LineColor``
     - ``color``
   * - ``LineWidthMM``
     - ``double``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``SymbolFactor``
     - ``double``
   * - ``Tk``
     - ``string``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``bz.Eps``
     - ``single``
   * - ``bz.Fk``
     - ``string``

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
     - Value Types
   * - ``A``
     - ``single``
   * - ``Angle``
     - ``double``
   * - ``B``
     - ``single``
   * - ``Beschreibung``
     - ``string``
   * - ``C``
     - ``single``
   * - ``CPM``
     - ``double``
   * - ``Dphaus``
     - ``single``
   * - ``Dprlmin``
     - ``single``
   * - ``Dpvlmin``
     - ``single``
   * - ``Dtmin``
     - ``single``
   * - ``Fkcont``
     - ``string``
   * - ``Fktrft``
     - ``string``
   * - ``Fkzep1rl``
     - ``string``
   * - ``Fkzep1vl``
     - ``string``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``Idreferenz``
     - ``string``
   * - ``Imbg``
     - ``int32``
   * - ``InVariant``
     - ``boolean``
   * - ``Ind0``
     - ``int32``
   * - ``Indtr``
     - ``int32``
   * - ``IndtrKlartext``
     - ``string``
   * - ``Iplanung``
     - ``int32``
   * - ``Irfv``
     - ``int32``
   * - ``Lfk``
     - ``single``
   * - ``M0Estimated``
     - ``single``
   * - ``Name``
     - ``string``
   * - ``NumberOfVERB``
     - ``int32``
   * - ``P1soll``
     - ``single``
   * - ``Pk``
     - ``string``
   * - ``PositionOfDescription``
     - ``int32``
   * - ``Qm0``
     - ``single``
   * - ``Rho0``
     - ``single``
   * - ``ShowDescription``
     - ``boolean``
   * - ``SymbolFactor``
     - ``double``
   * - ``Tk``
     - ``string``
   * - ``Trs0``
     - ``single``
   * - ``Trsk``
     - ``single``
   * - ``Tsrl``
     - ``single``
   * - ``Tsvl``
     - ``single``
   * - ``Tvl0``
     - ``single``
   * - ``V0``
     - ``single``
   * - ``Vtyp``
     - ``int32``
   * - ``W0``
     - ``single``
   * - ``W0Estimated``
     - ``single``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``Zevk``
     - ``single``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.Fklfkt``
     - ``string``
   * - ``bz.Fklfkt2``
     - ``string``
   * - ``bz.Fkqvar``
     - ``string``
   * - ``bz.Fktevt``
     - ``string``
   * - ``bz.Indlast``
     - ``int32``
   * - ``bz.IndlastKlartext``
     - ``string``
   * - ``bz.Indlfkt2``
     - ``int32``

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

DistrictHeatingFeeder
^^^^^^^^^^^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``Angle``
     - ``double``
   * - ``Beschreibung``
     - ``string``
   * - ``Dn``
     - ``single``
   * - ``Fkcont``
     - ``string``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Iplanung``
     - ``int32``
   * - ``Irueck``
     - ``int32``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``PositionOfDescription``
     - ``int32``
   * - ``ShowDescription``
     - ``boolean``
   * - ``SymbolFactor``
     - ``double``
   * - ``Taus``
     - ``single``
   * - ``Tk``
     - ``string``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``Zeta``
     - ``single``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.Fktevt``
     - ``string``
   * - ``bz.Fkwevt``
     - ``string``
   * - ``bz.Ihytyp``
     - ``int32``
   * - ``bz.IhytypKlartext``
     - ``string``
   * - ``bz.Ithtyp``
     - ``int32``
   * - ``bz.IthtypKlartext``
     - ``string``
   * - ``bz.Tkon``
     - ``single``
   * - ``bz.Wkon``
     - ``single``

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

Divider
^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``Angle``
     - ``double``
   * - ``Beschreibung``
     - ``string``
   * - ``E1``
     - ``string``
   * - ``E2``
     - ``string``
   * - ``Fkcont``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Inddiv``
     - ``int32``
   * - ``Ka``
     - ``string``
   * - ``Mindiv``
     - ``single``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``RglSymbolTyp``
     - ``rglsymboltype``
   * - ``SymbolFactor``
     - ``double``
   * - ``Tk``
     - ``string``
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

DriveEfficiencyTable
^^^^^^^^^^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``Beschreibung``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Tk``
     - ``string``
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
     - Value Types
   * - ``Etam``
     - ``single``
   * - ``Fk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Name``
     - ``string``
   * - ``Nzun0``
     - ``single``
   * - ``Pk``
     - ``string``

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
     - Value Types
   * - ``Beschreibung``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Tk``
     - ``string``
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
     - Value Types
   * - ``Fk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Name``
     - ``string``
   * - ``Pamax``
     - ``single``
   * - ``Pk``
     - ``string``
   * - ``Tumg``
     - ``single``

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
     - Value Types
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Lfdnr``
     - ``int32``
   * - ``Name``
     - ``string``
   * - ``ObjsString``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``bz.Aktiv``
     - ``int32``
   * - ``bz.Aktivqs``
     - ``int32``
   * - ``bz.Fk``
     - ``string``
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
     - Value Types
   * - ``Beschreibung``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Tk``
     - ``string``
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
     - Value Types
   * - ``Etafu``
     - ``single``
   * - ``Fk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Name``
     - ``string``
   * - ``Nzun0``
     - ``single``
   * - ``Pk``
     - ``string``

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
     - Value Types
   * - ``Aktiv``
     - ``int32``
   * - ``Elementtype``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Lfdnr``
     - ``int32``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``QueryStringAsString``
     - ``string``

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
     - Value Types
   * - ``Beschreibung``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Tk``
     - ``string``
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
     - Value Types
   * - ``Etadt``
     - ``single``
   * - ``Fk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Name``
     - ``string``
   * - ``Nzun0``
     - ``single``
   * - ``Pk``
     - ``string``

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
     - Value Types
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.Fktevt``
     - ``string``
   * - ``bz.Fkwttr``
     - ``string``
   * - ``bz.Indi``
     - ``int32``
   * - ``bz.Tu``
     - ``single``

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
     - Value Types
   * - ``Ahausg``
     - ``single``
   * - ``Arohr``
     - ``single``
   * - ``Flfwvb``
     - ``single``
   * - ``Hgebzg``
     - ``single``
   * - ``Ikotyp``
     - ``int32``
   * - ``InVariant``
     - ``boolean``
   * - ``Lambdabzg``
     - ``single``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Rhobzg``
     - ``single``
   * - ``Vhausg``
     - ``single``
   * - ``Zerohr``
     - ``single``

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
     - Value Types
   * - ``Angle``
     - ``double``
   * - ``Beschreibung``
     - ``string``
   * - ``Dn``
     - ``single``
   * - ``Fkcont``
     - ``string``
   * - ``Fkphiv``
     - ``string``
   * - ``Fkzep2``
     - ``string``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Iplanung``
     - ``int32``
   * - ``Name``
     - ``string``
   * - ``Phie``
     - ``single``
   * - ``Pk``
     - ``string``
   * - ``PositionOfDescription``
     - ``int32``
   * - ``ShowDescription``
     - ``boolean``
   * - ``SymbolFactor``
     - ``double``
   * - ``Te``
     - ``single``
   * - ``Tk``
     - ``string``
   * - ``Ts``
     - ``single``
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

FlowControlUnit
^^^^^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``Angle``
     - ``double``
   * - ``Beschreibung``
     - ``string``
   * - ``Dn``
     - ``single``
   * - ``Dqdt``
     - ``single``
   * - ``Fkcont``
     - ``string``
   * - ``Fkzep1``
     - ``string``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Iplanung``
     - ``int32``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``PositionOfDescription``
     - ``int32``
   * - ``ShowDescription``
     - ``boolean``
   * - ``SymbolFactor``
     - ``double``
   * - ``Tk``
     - ``string``
   * - ``Tsig``
     - ``single``
   * - ``Tvoll``
     - ``single``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.Fkswvtphi``
     - ``string``
   * - ``bz.Fkswvtqm``
     - ``string``
   * - ``bz.Indsoll``
     - ``int32``
   * - ``bz.Phisoll``
     - ``single``
   * - ``bz.Qmsoll``
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

FluidQualityParamSet
^^^^^^^^^^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``Chlorid``
     - ``single``
   * - ``Eisenfilt``
     - ``single``
   * - ``Eisenges``
     - ``single``
   * - ``Hi``
     - ``single``
   * - ``Hs``
     - ``single``
   * - ``InVariant``
     - ``boolean``
   * - ``Indchlorid``
     - ``int32``
   * - ``Indeisenfilt``
     - ``int32``
   * - ``Indeisenges``
     - ``int32``
   * - ``Indhi``
     - ``int32``
   * - ``Indhs``
     - ``int32``
   * - ``Indleitfaeh``
     - ``int32``
   * - ``Indmn``
     - ``int32``
   * - ``Indphwert``
     - ``int32``
   * - ``Indrhon``
     - ``int32``
   * - ``Indsulfat``
     - ``int32``
   * - ``Indtemp``
     - ``int32``
   * - ``Leitfaeh``
     - ``single``
   * - ``Lfdnr``
     - ``int32``
   * - ``Mn``
     - ``int32``
   * - ``Name``
     - ``string``
   * - ``Phwert``
     - ``single``
   * - ``Pk``
     - ``string``
   * - ``Rhon``
     - ``single``
   * - ``Sulfat``
     - ``single``
   * - ``Temp``
     - ``single``
   * - ``Tk``
     - ``string``
   * - ``Walter``
     - ``single``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.Fkswvtchlorid``
     - ``string``
   * - ``bz.Fkswvteisenfilt``
     - ``string``
   * - ``bz.Fkswvteisenges``
     - ``string``
   * - ``bz.Fkswvthi``
     - ``string``
   * - ``bz.Fkswvths``
     - ``string``
   * - ``bz.Fkswvtleitfaeh``
     - ``string``
   * - ``bz.Fkswvtmn``
     - ``string``
   * - ``bz.Fkswvtphwert``
     - ``string``
   * - ``bz.Fkswvtrhon``
     - ``string``
   * - ``bz.Fkswvtsulfat``
     - ``string``
   * - ``bz.Fkswvttemp``
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

FluidQualityParamSet_OS
^^^^^^^^^^^^^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``Fk``
     - ``string``
   * - ``Fkswvtchlorid``
     - ``string``
   * - ``Fkswvteisenfilt``
     - ``string``
   * - ``Fkswvteisenges``
     - ``string``
   * - ``Fkswvthi``
     - ``string``
   * - ``Fkswvths``
     - ``string``
   * - ``Fkswvtleitfaeh``
     - ``string``
   * - ``Fkswvtmn``
     - ``string``
   * - ``Fkswvtphwert``
     - ``string``
   * - ``Fkswvtrhon``
     - ``string``
   * - ``Fkswvtsulfat``
     - ``string``
   * - ``Fkswvttemp``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``

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
     - Value Types
   * - ``Cp``
     - ``single``
   * - ``Dracoeffa``
     - ``single``
   * - ``Dracoeffb``
     - ``single``
   * - ``Dracoeffc``
     - ``single``
   * - ``Dynvisko``
     - ``single``
   * - ``Eps``
     - ``single``
   * - ``Fkgmix``
     - ``string``
   * - ``Fkstof``
     - ``string``
   * - ``Gkomp1``
     - ``single``
   * - ``Gkomp2``
     - ``single``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Indstf``
     - ``int32``
   * - ``Isotherm``
     - ``single``
   * - ``K``
     - ``single``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Pref``
     - ``single``
   * - ``Rhonorm``
     - ``single``
   * - ``Tabdnam``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Tref``
     - ``single``

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
     - Value Types
   * - ``Beschreibung``
     - ``string``
   * - ``BoundingRectangle``
     - ``irectangle``
   * - ``Cdim``
     - ``string``
   * - ``ElementFont``
     - ``c3sfont``
   * - ``Fkcont``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Name``
     - ``string``
   * - ``Oalm``
     - ``single``
   * - ``Owarn``
     - ``single``
   * - ``Pk``
     - ``string``
   * - ``Showname``
     - ``int32``
   * - ``Showrect``
     - ``int32``
   * - ``T``
     - ``single``
   * - ``Tk``
     - ``string``
   * - ``Ualm``
     - ``single``
   * - ``Uwarn``
     - ``single``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``bz.Afakt``
     - ``single``
   * - ``bz.Dt``
     - ``single``
   * - ``bz.Dy``
     - ``single``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.Fkwtab``
     - ``string``
   * - ``bz.Ityp``
     - ``int32``
   * - ``bz.Wert``
     - ``single``

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

FunctionGenerator
^^^^^^^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``Angle``
     - ``double``
   * - ``Beschreibung``
     - ``string``
   * - ``E1``
     - ``string``
   * - ``Fkcont``
     - ``string``
   * - ``Fktfkt``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Indfkt``
     - ``int32``
   * - ``Ka``
     - ``string``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``RglSymbolTyp``
     - ``rglsymboltype``
   * - ``SymbolFactor``
     - ``double``
   * - ``Tk``
     - ``string``
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

FunctionTable
^^^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``Beschreibung``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Tk``
     - ``string``
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
     - Value Types
   * - ``Fk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``X``
     - ``single``
   * - ``Y``
     - ``single``

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
     - Value Types
   * - ``BwrA``
     - ``single``
   * - ``BwrA0``
     - ``single``
   * - ``BwrAlpha``
     - ``single``
   * - ``BwrB``
     - ``single``
   * - ``BwrB0``
     - ``single``
   * - ``BwrC``
     - ``single``
   * - ``BwrC0``
     - ``single``
   * - ``BwrGamma``
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
   * - ``Formula``
     - ``string``
   * - ``Hi``
     - ``single``
   * - ``Hs``
     - ``single``
   * - ``InVariant``
     - ``boolean``
   * - ``Lfdnr``
     - ``int32``
   * - ``Molarmass``
     - ``single``
   * - ``Name``
     - ``string``
   * - ``Pc``
     - ``single``
   * - ``Pk``
     - ``string``
   * - ``Tb``
     - ``single``
   * - ``Tc``
     - ``single``
   * - ``Tk``
     - ``string``
   * - ``Zisocoef``
     - ``single``

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
     - Value Types
   * - ``Beschreibung``
     - ``string``
   * - ``Fkgkmp1``
     - ``string``
   * - ``Fkgkmp10``
     - ``string``
   * - ``Fkgkmp11``
     - ``string``
   * - ``Fkgkmp12``
     - ``string``
   * - ``Fkgkmp13``
     - ``string``
   * - ``Fkgkmp14``
     - ``string``
   * - ``Fkgkmp15``
     - ``string``
   * - ``Fkgkmp16``
     - ``string``
   * - ``Fkgkmp17``
     - ``string``
   * - ``Fkgkmp18``
     - ``string``
   * - ``Fkgkmp19``
     - ``string``
   * - ``Fkgkmp2``
     - ``string``
   * - ``Fkgkmp20``
     - ``string``
   * - ``Fkgkmp21``
     - ``string``
   * - ``Fkgkmp22``
     - ``string``
   * - ``Fkgkmp3``
     - ``string``
   * - ``Fkgkmp4``
     - ``string``
   * - ``Fkgkmp5``
     - ``string``
   * - ``Fkgkmp6``
     - ``string``
   * - ``Fkgkmp7``
     - ``string``
   * - ``Fkgkmp8``
     - ``string``
   * - ``Fkgkmp9``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Lfdnr``
     - ``int32``
   * - ``Molfrac1``
     - ``single``
   * - ``Molfrac10``
     - ``single``
   * - ``Molfrac11``
     - ``single``
   * - ``Molfrac12``
     - ``single``
   * - ``Molfrac13``
     - ``single``
   * - ``Molfrac14``
     - ``single``
   * - ``Molfrac15``
     - ``single``
   * - ``Molfrac16``
     - ``single``
   * - ``Molfrac17``
     - ``single``
   * - ``Molfrac18``
     - ``single``
   * - ``Molfrac19``
     - ``single``
   * - ``Molfrac2``
     - ``single``
   * - ``Molfrac20``
     - ``single``
   * - ``Molfrac21``
     - ``single``
   * - ``Molfrac22``
     - ``single``
   * - ``Molfrac3``
     - ``single``
   * - ``Molfrac4``
     - ``single``
   * - ``Molfrac5``
     - ``single``
   * - ``Molfrac6``
     - ``single``
   * - ``Molfrac7``
     - ``single``
   * - ``Molfrac8``
     - ``single``
   * - ``Molfrac9``
     - ``single``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Tk``
     - ``string``

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
     - Value Types
   * - ``Forc``
     - ``int32``
   * - ``Idph``
     - ``int32``
   * - ``Idqm``
     - ``int32``
   * - ``InVariant``
     - ``boolean``
   * - ``Name``
     - ``string``
   * - ``Netztyp``
     - ``int32``
   * - ``Pfadol1``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``bz.ArtTh``
     - ``int32``
   * - ``bz.CalcNetwork``
     - ``int32``
   * - ``bz.Cdat``
     - ``string``
   * - ``bz.CheckMod``
     - ``int32``
   * - ``bz.CheckRes``
     - ``int32``
   * - ``bz.Cuhr``
     - ``string``
   * - ``bz.Czon``
     - ``string``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.Iart``
     - ``int32``
   * - ``bz.Idra``
     - ``int32``
   * - ``bz.Itrenn``
     - ``int32``
   * - ``bz.Jwarn``
     - ``int32``
   * - ``bz.Knuvtyp``
     - ``int32``
   * - ``bz.Lfqsv``
     - ``single``
   * - ``bz.Schwellqsig``
     - ``single``
   * - ``bz.ThInst``
     - ``int32``
   * - ``bz.ThStat``
     - ``int32``
   * - ``bz.Thfakt``
     - ``int32``
   * - ``bz.ValidAggr``
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

Gravitation
^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``Beschx``
     - ``single``
   * - ``Beschy``
     - ``single``
   * - ``Beschz``
     - ``single``
   * - ``InVariant``
     - ``boolean``
   * - ``Jgrav``
     - ``int32``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``

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
     - Value Types
   * - ``A``
     - ``single``
   * - ``Alpha1``
     - ``single``
   * - ``Alpha2``
     - ``single``
   * - ``Angle``
     - ``double``
   * - ``Beschreibung``
     - ``string``
   * - ``Dn``
     - ``single``
   * - ``Dp10min``
     - ``single``
   * - ``Dp20``
     - ``single``
   * - ``Expert``
     - ``int32``
   * - ``Fkcont``
     - ``string``
   * - ``Fkfwes``
     - ``string``
   * - ``Fkfwvb``
     - ``string``
   * - ``Fkzep1rl``
     - ``single``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Inddprl``
     - ``int32``
   * - ``Indwue``
     - ``int32``
   * - ``Iplanung``
     - ``int32``
   * - ``K``
     - ``single``
   * - ``Kstrant``
     - ``single``
   * - ``L1``
     - ``single``
   * - ``L2``
     - ``single``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``PositionOfDescription``
     - ``int32``
   * - ``Re0``
     - ``single``
   * - ``ShowDescription``
     - ``boolean``
   * - ``SymbolFactor``
     - ``double``
   * - ``T1aus0``
     - ``single``
   * - ``T1ein0``
     - ``single``
   * - ``T2aus0``
     - ``single``
   * - ``T2ein0``
     - ``single``
   * - ``Tk``
     - ``string``
   * - ``Tsrl``
     - ``single``
   * - ``W0``
     - ``single``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``bz.Einaus``
     - ``int32``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.Fktevt``
     - ``string``
   * - ``bz.Ithtyp``
     - ``int32``
   * - ``bz.T2aus``
     - ``single``

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

HeatFeederConsumerStation
^^^^^^^^^^^^^^^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``Abrutto``
     - ``single``
   * - ``Angle``
     - ``double``
   * - ``Beschreibung``
     - ``string``
   * - ``Deta0bLost``
     - ``single``
   * - ``Dhbasis``
     - ``single``
   * - ``Di``
     - ``single``
   * - ``Dn``
     - ``single``
   * - ``Dpes0``
     - ``single``
   * - ``Dpvb0min``
     - ``single``
   * - ``Dtsett``
     - ``single``
   * - ``Dtwt``
     - ``single``
   * - ``Fkcont``
     - ``string``
   * - ``Fkfwes``
     - ``string``
   * - ``Fkfwvb``
     - ``string``
   * - ``Fkklap``
     - ``string``
   * - ``Fkpreg``
     - ``string``
   * - ``Fkpump``
     - ``string``
   * - ``Fksoko``
     - ``string``
   * - ``Fktrft``
     - ``string``
   * - ``Fkzep1Pr``
     - ``string``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``Gtmaxtset``
     - ``single``
   * - ``HBUkDif``
     - ``single``
   * - ``HDif``
     - ``single``
   * - ``HMantel``
     - ``single``
   * - ``HWsMax``
     - ``single``
   * - ``HWsOkDif``
     - ``single``
   * - ``He``
     - ``single``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Indrohr``
     - ``int32``
   * - ``Indrumg``
     - ``int32``
   * - ``Indtr``
     - ``int32``
   * - ``Indtrack``
     - ``int32``
   * - ``Indtset``
     - ``int32``
   * - ``Indusing``
     - ``int32``
   * - ``Indwt``
     - ``int32``
   * - ``Iplanung``
     - ``int32``
   * - ``Kr``
     - ``single``
   * - ``KrKt``
     - ``single``
   * - ``L``
     - ``single``
   * - ``Lambdad``
     - ``single``
   * - ``Lambdae``
     - ``single``
   * - ``Medium``
     - ``int32``
   * - ``Name``
     - ``string``
   * - ``NodeNameI``
     - ``string``
   * - ``NodeNameK``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``PositionOfDescription``
     - ``int32``
   * - ``PrDn``
     - ``single``
   * - ``PuHref``
     - ``single``
   * - ``PuNref``
     - ``single``
   * - ``PuPref``
     - ``single``
   * - ``PuQmref``
     - ``single``
   * - ``Qfs``
     - ``single``
   * - ``RDif``
     - ``single``
   * - ``RInnen``
     - ``single``
   * - ``Rd``
     - ``single``
   * - ``ShowDescription``
     - ``boolean``
   * - ``StorageType``
     - ``int32``
   * - ``SymbolFactor``
     - ``double``
   * - ``Tdr``
     - ``single``
   * - ``Tgrenz``
     - ``single``
   * - ``Tk``
     - ``string``
   * - ``Tob``
     - ``single``
   * - ``TrefMin``
     - ``single``
   * - ``Trl0``
     - ``single``
   * - ``Trs0``
     - ``single``
   * - ``Tru``
     - ``single``
   * - ``Tsp0``
     - ``single``
   * - ``TtolEs``
     - ``single``
   * - ``TtolVb``
     - ``single``
   * - ``Tu``
     - ``single``
   * - ``Tvl0``
     - ``single``
   * - ``UBoden``
     - ``single``
   * - ``UMantel``
     - ``single``
   * - ``Volsp``
     - ``single``
   * - ``Vrv``
     - ``single``
   * - ``W0Es``
     - ``single``
   * - ``W0Sp``
     - ``single``
   * - ``W0Vb``
     - ``single``
   * - ``Wcorr``
     - ``single``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``bz.Azimut``
     - ``single``
   * - ``bz.Einaus``
     - ``int32``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.Fklfkt``
     - ``string``
   * - ``bz.FkqvarSp``
     - ``string``
   * - ``bz.FktevtEs``
     - ``string``
   * - ``bz.FktevtRs``
     - ``string``
   * - ``bz.FkwevtEs``
     - ``string``
   * - ``bz.FkwevtSp``
     - ``string``
   * - ``bz.FkwevtVb``
     - ``string``
   * - ``bz.Fkwttr``
     - ``string``
   * - ``bz.HWsStart``
     - ``single``
   * - ``bz.Indlast``
     - ``int32``
   * - ``bz.IndsSp``
     - ``int32``
   * - ``bz.Indstagn``
     - ``int32``
   * - ``bz.Ithtyp``
     - ``int32``
   * - ``bz.ModeSp``
     - ``int32``
   * - ``bz.Neigung``
     - ``single``
   * - ``bz.Ppumax``
     - ``single``
   * - ``bz.Pvlmax``
     - ``single``
   * - ``bz.Qsprel0``
     - ``single``
   * - ``bz.TobStart``
     - ``single``
   * - ``bz.TrsMax``
     - ``single``
   * - ``bz.TspMin``
     - ``single``
   * - ``bz.TtolEval``
     - ``single``
   * - ``bz.TuStart``
     - ``single``
   * - ``bz.TzuMax``
     - ``single``
   * - ``bz.TzuMin``
     - ``single``
   * - ``bz.W0SpMin``
     - ``single``

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
   * - ``Q_PU``
   * - ``TDIFFO``
   * - ``TDIFFU``
   * - ``TRL``
   * - ``TRS``
   * - ``TSP``
   * - ``TVEC``
   * - ``TVL``
   * - ``T_KALT``
   * - ``T_MIX``
   * - ``T_WARM``
   * - ``W``
   * - ``WKOLL``
   * - ``W_ES``
   * - ``W_FS``
   * - ``W_PR``
   * - ``W_RO``
   * - ``W_VB``

HeaterCooler
^^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``Angle``
     - ``double``
   * - ``Beschreibung``
     - ``string``
   * - ``Dpnum``
     - ``single``
   * - ``Eta``
     - ``single``
   * - ``Fkcont``
     - ``string``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Iplanung``
     - ``int32``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``PositionOfDescription``
     - ``int32``
   * - ``ShowDescription``
     - ``boolean``
   * - ``SymbolFactor``
     - ``double``
   * - ``Tk``
     - ``string``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
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

Histeresis
^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``Angle``
     - ``double``
   * - ``Beschreibung``
     - ``string``
   * - ``E1``
     - ``string``
   * - ``Fkcont``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Indhys``
     - ``int32``
   * - ``Ka``
     - ``string``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``RglSymbolTyp``
     - ``rglsymboltype``
   * - ``SymbolFactor``
     - ``double``
   * - ``Tk``
     - ``string``
   * - ``Xkor``
     - ``double``
   * - ``Xo``
     - ``single``
   * - ``Xstart``
     - ``single``
   * - ``Xu``
     - ``single``
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

House
^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``DsnBundesweit``
     - ``string``
   * - ``Fkfwvb``
     - ``string``
   * - ``Fkknot``
     - ``string``
   * - ``Fkstrasse``
     - ``string``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``Graphics``
     - ``hausverbgraf``
   * - ``Hausnr``
     - ``int32``
   * - ``HausnrZus``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Plz``
     - ``int32``
   * - ``SymbolFactor``
     - ``double``
   * - ``Tk``
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
     - Value Types
   * - ``Angle``
     - ``double``
   * - ``Beschreibung``
     - ``string``
   * - ``Dn``
     - ``single``
   * - ``FkdtroRowd``
     - ``string``
   * - ``Fkknot``
     - ``string``
   * - ``Fkrohr``
     - ``string``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``L``
     - ``single``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Poskm``
     - ``single``
   * - ``Rau``
     - ``single``
   * - ``SymbolFactor``
     - ``double``
   * - ``Tk``
     - ``string``
   * - ``Typ``
     - ``int32``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``Zeta``
     - ``single``
   * - ``Zkor``
     - ``single``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.Fkswvt``
     - ``string``
   * - ``bz.Iaktiv``
     - ``int32``
   * - ``bz.Indi``
     - ``int32``
   * - ``bz.PhMin``
     - ``single``
   * - ``bz.Phsoll``
     - ``single``
   * - ``bz.Qmsoll``
     - ``single``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``BCTYP``
   * - ``IAKTIV``
   * - ``MAINELEMENT``
   * - ``PHR``
   * - ``PHR_ROHR``
   * - ``PHSOLL``
   * - ``PH_EINB``
   * - ``PH_ENTN``
   * - ``PH_MIN``
   * - ``QM``
   * - ``QSOLL``
   * - ``UV``

Integrator
^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``Angle``
     - ``double``
   * - ``Beschreibung``
     - ``string``
   * - ``E1``
     - ``string``
   * - ``Fkcont``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Ka``
     - ``string``
   * - ``Name``
     - ``string``
   * - ``Ogr``
     - ``single``
   * - ``Pk``
     - ``string``
   * - ``RglSymbolTyp``
     - ``rglsymboltype``
   * - ``SymbolFactor``
     - ``double``
   * - ``Tk``
     - ``string``
   * - ``Ugr``
     - ``single``
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

LAYR_Layer
^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Lfdnr``
     - ``int32``
   * - ``Name``
     - ``string``
   * - ``ObjsString``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Setzen``
     - ``int32``
   * - ``Tk``
     - ``string``
   * - ``Zeigen``
     - ``int32``

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
     - Value Types
   * - ``Beschreibung``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Intpol``
     - ``int32``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Zeitoption``
     - ``int32``

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

LoadFactorTable_Row
^^^^^^^^^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``Fk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Lf``
     - ``single``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Zeit``
     - ``single``
   * - ``Zeitstempel``
     - ``string``

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
     - Value Types
   * - ``Angle``
     - ``double``
   * - ``Beschreibung``
     - ``string``
   * - ``E1``
     - ``string``
   * - ``E2``
     - ``string``
   * - ``Fkcont``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Indtyp``
     - ``int32``
   * - ``Ka``
     - ``string``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``RglSymbolTyp``
     - ``rglsymboltype``
   * - ``SymbolFactor``
     - ``double``
   * - ``Tk``
     - ``string``
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

LogicalStorage
^^^^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``Angle``
     - ``double``
   * - ``Beschreibung``
     - ``string``
   * - ``E1``
     - ``string``
   * - ``E2``
     - ``string``
   * - ``Fkcont``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Ka``
     - ``string``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``RglSymbolTyp``
     - ``rglsymboltype``
   * - ``SymbolFactor``
     - ``double``
   * - ``Tk``
     - ``string``
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

MeasuredVariableTable
^^^^^^^^^^^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``Beschreibung``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Intpol``
     - ``int32``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Zeitoption``
     - ``int32``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``MAINELEMENT``
   * - ``W``

MeasuredVariableTable_Row
^^^^^^^^^^^^^^^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``Fk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``W``
     - ``single``
   * - ``Zeit``
     - ``single``
   * - ``Zeitstempel``
     - ``string``

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
     - Value Types
   * - ``Angle``
     - ``double``
   * - ``Beschreibung``
     - ``string``
   * - ``E1``
     - ``string``
   * - ``E2``
     - ``string``
   * - ``Fkcont``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Indmma``
     - ``int32``
   * - ``Ka``
     - ``string``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``RglSymbolTyp``
     - ``rglsymboltype``
   * - ``SymbolFactor``
     - ``double``
   * - ``Tk``
     - ``string``
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

Multiplier
^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``Angle``
     - ``double``
   * - ``Beschreibung``
     - ``string``
   * - ``E1``
     - ``string``
   * - ``E2``
     - ``string``
   * - ``Fkcont``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Indmul``
     - ``int32``
   * - ``Ka``
     - ``string``
   * - ``Konst``
     - ``single``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``RglSymbolTyp``
     - ``rglsymboltype``
   * - ``SymbolFactor``
     - ``double``
   * - ``Tk``
     - ``string``
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

NetValve
^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``Beschreibung``
     - ``string``
   * - ``Fkrohr``
     - ``string``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Poskm``
     - ``single``
   * - ``SymbolFactor``
     - ``double``
   * - ``Tk``
     - ``string``
   * - ``Typ``
     - ``int32``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.Fkswvt``
     - ``string``
   * - ``bz.Indi``
     - ``int32``
   * - ``bz.Stellung``
     - ``int32``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``MAINELEMENT``
   * - ``STELLUNG``

Node
^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``Beschreibung``
     - ``string``
   * - ``Fk2lknot``
     - ``string``
   * - ``Fkcont``
     - ``string``
   * - ``Fkfqps``
     - ``string``
   * - ``Fkfstf``
     - ``string``
   * - ``Fkpzon``
     - ``string``
   * - ``Fkutmp``
     - ``string``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``HasBlockConnection``
     - ``boolean``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Iplanung``
     - ``int32``
   * - ``Ktyp``
     - ``string``
   * - ``Kvr``
     - ``int32``
   * - ``KvrKlartext``
     - ``string``
   * - ``Lfakt``
     - ``single``
   * - ``Name``
     - ``string``
   * - ``NodeNamePosition``
     - ``int32``
   * - ``NumberOfVERB``
     - ``int32``
   * - ``Pk``
     - ``string``
   * - ``Qakt``
     - ``double``
   * - ``QmEin``
     - ``single``
   * - ``ShowNodeName``
     - ``boolean``
   * - ``SymbolFactor``
     - ``double``
   * - ``Tk``
     - ``string``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``Zkor``
     - ``single``
   * - ``bz.Drakonz``
     - ``single``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.Fklfkt``
     - ``string``
   * - ``bz.Fkpvar``
     - ``string``
   * - ``bz.Fkqvar``
     - ``string``
   * - ``bz.PhEin``
     - ``single``
   * - ``bz.PhMin``
     - ``single``
   * - ``bz.Te``
     - ``single``
   * - ``bz.Tm``
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
   * - ``PHMINMAXDIF``
   * - ``PHWERT``
   * - ``PH_EIN``
   * - ``PH_MIN``
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

NonReturnValvesTable
^^^^^^^^^^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``Beschreibung``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Tk``
     - ``string``

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
     - Value Types
   * - ``Fk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Name``
     - ``string``
   * - ``Phi``
     - ``single``
   * - ``Pk``
     - ``string``
   * - ``V``
     - ``single``

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
     - Value Types
   * - ``Abswert``
     - ``int32``
   * - ``Alarmcolor``
     - ``int32``
   * - ``Angle``
     - ``double``
   * - ``Attrtype``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``BoundingRectangle``
     - ``irectangle``
   * - ``Checkcolor``
     - ``int32``
   * - ``Decpoint``
     - ``int32``
   * - ``ElementAlarmColor``
     - ``color``
   * - ``ElementFont``
     - ``c3sfont``
   * - ``ElementNoticeColor``
     - ``color``
   * - ``ElementWarnColor``
     - ``color``
   * - ``Fkcont``
     - ``string``
   * - ``FkdpgrDpkt``
     - ``string``
   * - ``Fkobjtype``
     - ``string``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``InVariant``
     - ``boolean``
   * - ``Indval``
     - ``int32``
   * - ``Name``
     - ``string``
   * - ``Noticecolor``
     - ``int32``
   * - ``Objtype``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``PrefixWidth``
     - ``double``
   * - ``Prftxt``
     - ``string``
   * - ``ResultValue``
     - ``string``
   * - ``Thousandsep``
     - ``int32``
   * - ``Tk``
     - ``string``
   * - ``Unit``
     - ``string``
   * - ``Warncolor``
     - ``int32``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
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
     - Value Types
   * - ``BoundingRectangle``
     - ``irectangle``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``Id``
     - ``int32``
   * - ``Idparent``
     - ``int32``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Lfdnr``
     - ``int32``
   * - ``MaximalNodeWidth``
     - ``double``
   * - ``MaximalPipeWidth``
     - ``double``
   * - ``MaximalVbelNselWidth``
     - ``double``
   * - ``MeterPerPixel``
     - ``double``
   * - ``Name``
     - ``string``
   * - ``PickingTolerance``
     - ``double``
   * - ``Pk``
     - ``string``
   * - ``SymbolFont``
     - ``c3sfont``
   * - ``SymbolType``
     - ``ccontsymboltype``
   * - ``Tk``
     - ``string``
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
     - Value Types
   * - ``A``
     - ``single``
   * - ``Angle``
     - ``double``
   * - ``Beschreibung``
     - ``string``
   * - ``Dn``
     - ``single``
   * - ``Filling``
     - ``int32``
   * - ``Fkatab``
     - ``string``
   * - ``Fkcont``
     - ``string``
   * - ``Fkfstf``
     - ``string``
   * - ``Fkknotfilling``
     - ``string``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``Hb``
     - ``single``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Indatab``
     - ``int32``
   * - ``Iplanung``
     - ``int32``
   * - ``Knotk``
     - ``string``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``SymbolFactor``
     - ``double``
   * - ``SymbolGraf``
     - ``symbol1c_graf``
   * - ``Tk``
     - ``string``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``Zetaneg``
     - ``single``
   * - ``Zetapos``
     - ``single``
   * - ``Zkor``
     - ``single``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.Tm0``
     - ``single``
   * - ``bz.Walter0``
     - ``single``
   * - ``bz.Wsp``
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

Oval
^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``Beschreibung``
     - ``string``
   * - ``Fkcont``
     - ``string``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Tk``
     - ``string``
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
     - Value Types
   * - ``InVariant``
     - ``boolean``
   * - ``Jdampf``
     - ``int32``
   * - ``Jrst``
     - ``int32``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Thepdk``
     - ``single``
   * - ``Thepdr``
     - ``single``
   * - ``bz.Dt``
     - ``single``
   * - ``bz.Dttrsp``
     - ``single``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.Tmax``
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
     - Value Types
   * - ``Angle``
     - ``double``
   * - ``Beschreibung``
     - ``string``
   * - ``Dn``
     - ``single``
   * - ``Fkcont``
     - ``string``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Iplanung``
     - ``int32``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``PositionOfDescription``
     - ``int32``
   * - ``ShowDescription``
     - ``boolean``
   * - ``SymbolFactor``
     - ``double``
   * - ``Tk``
     - ``string``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``Zeta``
     - ``single``
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

PidController
^^^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``Angle``
     - ``double``
   * - ``Beschreibung``
     - ``string``
   * - ``E1``
     - ``string``
   * - ``E2``
     - ``string``
   * - ``Fkcont``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Inddif``
     - ``int32``
   * - ``Indein``
     - ``int32``
   * - ``Indint``
     - ``int32``
   * - ``Ka``
     - ``string``
   * - ``Kd``
     - ``single``
   * - ``Kp``
     - ``single``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``RglSymbolTyp``
     - ``rglsymboltype``
   * - ``SymbolFactor``
     - ``double``
   * - ``Td``
     - ``single``
   * - ``Tk``
     - ``string``
   * - ``Wirk``
     - ``int32``
   * - ``Xdzul``
     - ``single``
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

Pipe
^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``Asoll``
     - ``single``
   * - ``Baujahr``
     - ``string``
   * - ``Beschreibung``
     - ``string``
   * - ``DN``
     - ``string``
   * - ``Di``
     - ``single``
   * - ``DottedLine``
     - ``int32``
   * - ``Fk2lrohr``
     - ``string``
   * - ``Fkcont``
     - ``string``
   * - ``FkdtroRowd``
     - ``string``
   * - ``Fkltgr``
     - ``string``
   * - ``Fkstrasse``
     - ``string``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``Hal``
     - ``int32``
   * - ``HasClosedNSCHs``
     - ``nullable`1``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Indschall``
     - ``int32``
   * - ``Iplanung``
     - ``int32``
   * - ``Jlambs``
     - ``int32``
   * - ``Kvr``
     - ``int32``
   * - ``KvrKlartext``
     - ``string``
   * - ``L``
     - ``single``
   * - ``Lambda0``
     - ``single``
   * - ``LineWidthMM``
     - ``double``
   * - ``Lzu``
     - ``single``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Rau``
     - ``single``
   * - ``Tk``
     - ``string``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``Zaus``
     - ``single``
   * - ``Zein``
     - ``single``
   * - ``Zuml``
     - ``single``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.ITrennWithNSCH``
     - ``int32``
   * - ``bz.Imptnz``
     - ``single``
   * - ``bz.Irtrenn``
     - ``int32``
   * - ``bz.Kantenzv``
     - ``double``
   * - ``bz.Leckend``
     - ``single``
   * - ``bz.Leckmenge``
     - ``single``
   * - ``bz.Leckort``
     - ``single``
   * - ``bz.Leckstart``
     - ``single``
   * - ``bz.Leckstatus``
     - ``int32``
   * - ``bz.Qsvb``
     - ``single``
   * - ``bz.Zvlimptnz``
     - ``double``

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

PipeGroup
^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``Beschreibung``
     - ``string``
   * - ``Fksrat``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Sichtbarkeit``
     - ``int32``
   * - ``Tk``
     - ``string``
   * - ``Verlegeart``
     - ``int32``

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
     - Value Types
   * - ``Beschreibung``
     - ``string``
   * - ``E``
     - ``single``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Typ``
     - ``string``
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
     - Value Types
   * - ``Ausfallzeit``
     - ``single``
   * - ``Da``
     - ``single``
   * - ``Di``
     - ``single``
   * - ``Dn``
     - ``string``
   * - ``Fk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Kt``
     - ``single``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Pn``
     - ``single``
   * - ``Rehabilitation``
     - ``single``
   * - ``Reparatur``
     - ``single``
   * - ``S``
     - ``single``
   * - ``Tk``
     - ``string``
   * - ``Wsteig``
     - ``single``
   * - ``Wtiefe``
     - ``single``

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
     - Value Types
   * - ``Fk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Lfdnr``
     - ``int32``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``Zkor``
     - ``single``

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

Polygon
^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``Beschreibung``
     - ``string``
   * - ``FillColor``
     - ``color``
   * - ``Fkcont``
     - ``string``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``LineColor``
     - ``color``
   * - ``LineWidthMM``
     - ``double``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Tk``
     - ``string``
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
     - Value Types
   * - ``Beschreibung``
     - ``string``
   * - ``DottedLine``
     - ``int32``
   * - ``Fkcont``
     - ``string``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``LineWidthMM``
     - ``double``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Tk``
     - ``string``
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
     - Value Types
   * - ``Angle``
     - ``double``
   * - ``Beschreibung``
     - ``string``
   * - ``Dn``
     - ``single``
   * - ``Fkcont``
     - ``string``
   * - ``Fkzep1``
     - ``string``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Indprg``
     - ``int32``
   * - ``Iplanung``
     - ``int32``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``PositionOfDescription``
     - ``int32``
   * - ``ShowDescription``
     - ``boolean``
   * - ``SymbolFactor``
     - ``double``
   * - ``Tk``
     - ``string``
   * - ``Ts``
     - ``single``
   * - ``Typ``
     - ``int32``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.Fkswvt``
     - ``string``
   * - ``bz.Indsoll``
     - ``int32``
   * - ``bz.Phsoll``
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

PressureZone
^^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``Idimbh``
     - ``int32``
   * - ``Idimra``
     - ``int32``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Klpmin``
     - ``single``
   * - ``Lfdnr``
     - ``int32``
   * - ``Modus``
     - ``int32``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Pkmaxbh``
     - ``single``
   * - ``Pkmaxra``
     - ``single``
   * - ``Pkminbh``
     - ``single``
   * - ``Pkminra``
     - ``single``
   * - ``Tk``
     - ``string``

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
     - Value Types
   * - ``Angle``
     - ``double``
   * - ``Beschreibung``
     - ``string``
   * - ``E1``
     - ``string``
   * - ``Fkcont``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Ka``
     - ``string``
   * - ``Kp``
     - ``single``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``RglSymbolTyp``
     - ``rglsymboltype``
   * - ``SymbolFactor``
     - ``double``
   * - ``T1``
     - ``single``
   * - ``Tk``
     - ``string``
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

Pump
^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``Angle``
     - ``double``
   * - ``BKFaktTubine``
     - ``single``
   * - ``Beschreibung``
     - ``string``
   * - ``Bkfak``
     - ``single``
   * - ``Dndt``
     - ``single``
   * - ``Dndtma``
     - ``single``
   * - ``Dngross``
     - ``single``
   * - ``Dnklein``
     - ``single``
   * - ``Dt0aus``
     - ``single``
   * - ``Dt0sch``
     - ``single``
   * - ``Dt0std``
     - ``single``
   * - ``EtaRef``
     - ``nullable`1``
   * - ``EtaRefTurb``
     - ``nullable`1``
   * - ``Etamot``
     - ``single``
   * - ``Fkcont``
     - ``string``
   * - ``Fketam``
     - ``string``
   * - ``Fketar``
     - ``string``
   * - ``Fketau``
     - ``string``
   * - ``Fkkiapd``
     - ``string``
   * - ``Fkkiaps``
     - ``string``
   * - ``Fkkiasf``
     - ``string``
   * - ``Fkkr1stf``
     - ``string``
   * - ``Fkkr3std``
     - ``string``
   * - ``Fkkr4std``
     - ``string``
   * - ``Fkkref1``
     - ``string``
   * - ``Fkkref2``
     - ``string``
   * - ``Fkkrsspd``
     - ``string``
   * - ``Fkkrssps``
     - ``string``
   * - ``Fkpumk``
     - ``string``
   * - ``Fkpumkturb``
     - ``string``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``Href``
     - ``single``
   * - ``Hrefturb``
     - ``single``
   * - ``Idreferenz``
     - ``string``
   * - ``Ifgsw``
     - ``int32``
   * - ``InVariant``
     - ``boolean``
   * - ``IndLTurb``
     - ``int32``
   * - ``Indapd``
     - ``int32``
   * - ``Indaps``
     - ``int32``
   * - ``Indasf``
     - ``int32``
   * - ``Indds``
     - ``int32``
   * - ``Indl``
     - ``int32``
   * - ``Indss``
     - ``int32``
   * - ``Indstd``
     - ``int32``
   * - ``Indstf``
     - ``int32``
   * - ``Iplanung``
     - ``int32``
   * - ``Jrlsp``
     - ``int32``
   * - ``Jwirk``
     - ``int32``
   * - ``Kdds``
     - ``single``
   * - ``Kdss``
     - ``single``
   * - ``Kdstd``
     - ``single``
   * - ``Kdstf``
     - ``single``
   * - ``Kids``
     - ``single``
   * - ``Kiss``
     - ``single``
   * - ``Kistd``
     - ``single``
   * - ``Kistf``
     - ``single``
   * - ``Kpds``
     - ``single``
   * - ``Kpss``
     - ``single``
   * - ``Kpstd``
     - ``single``
   * - ``Kpstf``
     - ``single``
   * - ``NMaxTurb``
     - ``single``
   * - ``NMinTurb``
     - ``single``
   * - ``Name``
     - ``string``
   * - ``Nemot``
     - ``single``
   * - ``Nmax``
     - ``single``
   * - ``Nmin``
     - ``single``
   * - ``Nref``
     - ``single``
   * - ``Nrefturb``
     - ``single``
   * - ``Ntrudel``
     - ``single``
   * - ``Papd``
     - ``single``
   * - ``Pdsein``
     - ``single``
   * - ``PerformanceMapParameters``
     - ``ipukennparams``
   * - ``Pk``
     - ``string``
   * - ``PositionOfDescription``
     - ``int32``
   * - ``Pref``
     - ``single``
   * - ``Prefturb``
     - ``single``
   * - ``Psa``
     - ``single``
   * - ``Pssein``
     - ``single``
   * - ``PukfString``
     - ``string``
   * - ``Q0MaxTurb``
     - ``single``
   * - ``Q0MinTurb``
     - ``single``
   * - ``Q0max``
     - ``single``
   * - ``Q0min``
     - ``single``
   * - ``Qmref``
     - ``single``
   * - ``Qmrefturb``
     - ``single``
   * - ``Schlupf``
     - ``single``
   * - ``ShowDescription``
     - ``boolean``
   * - ``SymbolFactor``
     - ``double``
   * - ``Tk``
     - ``string``
   * - ``Totapd``
     - ``single``
   * - ``Totaps``
     - ``single``
   * - ``Totasf``
     - ``single``
   * - ``Traeg``
     - ``single``
   * - ``Tsig``
     - ``single``
   * - ``Wirasf``
     - ``int32``
   * - ``Wirstd``
     - ``int32``
   * - ``Wirstf``
     - ``int32``
   * - ``Wscasf``
     - ``single``
   * - ``Wscstf``
     - ``single``
   * - ``Wsostd``
     - ``single``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.Fkpumd``
     - ``string``
   * - ``bz.Fkrcpl``
     - ``string``
   * - ``bz.Fkswvt``
     - ``string``
   * - ``bz.IndATurb``
     - ``int32``
   * - ``bz.IndSTurb``
     - ``int32``
   * - ``bz.Inda``
     - ``int32``
   * - ``bz.IndaKlartext``
     - ``string``
   * - ``bz.Inds``
     - ``int32``
   * - ``bz.IndsKlartext``
     - ``string``
   * - ``bz.Indturb``
     - ``int32``
   * - ``bz.Ispu``
     - ``int32``
   * - ``bz.IspuKlartext``
     - ``string``
   * - ``bz.Isputurb``
     - ``int32``
   * - ``bz.Nsoll``
     - ``single``
   * - ``bz.Nsollturb``
     - ``single``
   * - ``bz.Phsoll``
     - ``single``
   * - ``bz.Qmsoll``
     - ``single``
   * - ``bz.Qmsollturb``
     - ``single``
   * - ``bz.Tipu``
     - ``single``

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

PumpCharTable
^^^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``Beschreibung``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``N``
     - ``single``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Rhobzg``
     - ``single``
   * - ``Tk``
     - ``string``
   * - ``Typ``
     - ``int32``
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
     - Value Types
   * - ``Eta``
     - ``single``
   * - ``Fk``
     - ``string``
   * - ``H``
     - ``single``
   * - ``InVariant``
     - ``boolean``
   * - ``Name``
     - ``string``
   * - ``Npsh``
     - ``single``
   * - ``P``
     - ``single``
   * - ``Pk``
     - ``string``
   * - ``Q``
     - ``single``

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
     - Value Types
   * - ``ActAsa``
     - ``int32``
   * - ``AusAsa``
     - ``int32``
   * - ``Beschreibung``
     - ``string``
   * - ``BoundingRectangle``
     - ``irectangle``
   * - ``Dphaus``
     - ``single``
   * - ``Fkcont``
     - ``string``
   * - ``Fkkdmax``
     - ``string``
   * - ``Fkkibyp``
     - ``string``
   * - ``Fkkkbyp``
     - ``string``
   * - ``Fkksmin``
     - ``string``
   * - ``Ibyp``
     - ``int32``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Indrst``
     - ``int32``
   * - ``Iplanung``
     - ``int32``
   * - ``Ischalt``
     - ``int32``
   * - ``Name``
     - ``string``
   * - ``Nmax``
     - ``single``
   * - ``Pdmax``
     - ``single``
   * - ``Pk``
     - ``string``
   * - ``Psmin``
     - ``single``
   * - ``Qmaus``
     - ``single``
   * - ``Tk``
     - ``string``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.Fkrart``
     - ``string``
   * - ``bz.Iaktiv``
     - ``int32``
   * - ``bz.Indpg``
     - ``int32``

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

PumpOfPumpGroup
^^^^^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``Fkpgrp``
     - ``string``
   * - ``Fkpump``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Iplanung``
     - ``int32``
   * - ``Lfdnr``
     - ``int32``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
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

PumpSpeedTable
^^^^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``Beschreibung``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Intpol``
     - ``int32``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Zeitoption``
     - ``int32``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``MAINELEMENT``
   * - ``N``

PumpSpeedTable_Row
^^^^^^^^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``Fk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``N``
     - ``single``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Zeit``
     - ``single``
   * - ``Zeitstempel``
     - ``string``

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
     - Value Types
   * - ``Dt0reg``
     - ``single``
   * - ``FlagsUser``
     - ``int32``
   * - ``InVariant``
     - ``boolean``
   * - ``Indreg``
     - ``int32``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``

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
     - Value Types
   * - ``Addend``
     - ``single``
   * - ``AttributeDescription``
     - ``string``
   * - ``Factor``
     - ``single``
   * - ``Fkrmes``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Indfunc``
     - ``int32``
   * - ``Lfdnr``
     - ``int32``
   * - ``Name``
     - ``string``
   * - ``ObjectTypeDescription``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``bz.Attrtype``
     - ``string``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.Fkobjtype``
     - ``string``
   * - ``bz.Objtype``
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
     - Value Types
   * - ``Beschreibung``
     - ``string``
   * - ``FillColor``
     - ``color``
   * - ``Fkcont``
     - ``string``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``LineColor``
     - ``color``
   * - ``LineWidthMM``
     - ``double``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Tk``
     - ``string``
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
     - Value Types
   * - ``Beschreibung``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Kvbzg``
     - ``single``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Typ``
     - ``int32``
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
     - Value Types
   * - ``Fk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Kvrel``
     - ``single``
   * - ``Name``
     - ``string``
   * - ``Phi``
     - ``single``
   * - ``Pk``
     - ``string``
   * - ``Zeta``
     - ``single``

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
     - Value Types
   * - ``Beschreibung``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Tk``
     - ``string``
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
     - Value Types
   * - ``Fk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Lfth``
     - ``single``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Trs``
     - ``single``

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
     - Value Types
   * - ``Beschreibung``
     - ``string``
   * - ``FillColor``
     - ``color``
   * - ``Fkcont``
     - ``string``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``LineColor``
     - ``color``
   * - ``LineWidthMM``
     - ``double``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Tk``
     - ``string``
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
     - Value Types
   * - ``BlockBkgndColor``
     - ``int32``
   * - ``CacheDirectory``
     - ``string``
   * - ``CacheInUserProfile``
     - ``int32``
   * - ``DrawTileOutlines``
     - ``int32``
   * - ``HighlightElement``
     - ``int32``
   * - ``ImageQuality``
     - ``int32``
   * - ``InVariant``
     - ``boolean``
   * - ``LegFix``
     - ``int32``
   * - ``LegHeight``
     - ``single``
   * - ``LegMaxEntries``
     - ``int32``
   * - ``LegXkor``
     - ``double``
   * - ``LegYkor``
     - ``double``
   * - ``ListConfigString``
     - ``string``
   * - ``MaxLineSize``
     - ``int32``
   * - ``MaxNodeSize``
     - ``int32``
   * - ``MaxVbelSize``
     - ``int32``
   * - ``Name``
     - ``string``
   * - ``Nbnr``
     - ``int32``
   * - ``Nknr``
     - ``int32``
   * - ``OsmPasswd``
     - ``string``
   * - ``OsmTimeout``
     - ``int32``
   * - ``OsmUser``
     - ``string``
   * - ``PickingRadius``
     - ``int32``
   * - ``Pickingmode``
     - ``int32``
   * - ``Pk``
     - ``string``
   * - ``ProxyAuthMethod``
     - ``int32``
   * - ``ProxyPasswd``
     - ``string``
   * - ``ProxyServer``
     - ``string``
   * - ``ProxyUser``
     - ``string``
   * - ``Sccnln``
     - ``int32``
   * - ``Scelt``
     - ``int32``
   * - ``Scknot``
     - ``int32``
   * - ``Scrohr``
     - ``int32``
   * - ``Sfvbels``
     - ``double``
   * - ``Srid``
     - ``int32``
   * - ``Srid2``
     - ``int32``
   * - ``SridString``
     - ``string``
   * - ``StructuredViewsString``
     - ``string``
   * - ``Sylw``
     - ``single``
   * - ``TileDownloadServer``
     - ``string``
   * - ``Tooltip``
     - ``int32``
   * - ``Uimode``
     - ``int32``
   * - ``Upkc``
     - ``int32``
   * - ``UseHttpProxy``
     - ``int32``

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
     - Value Types
   * - ``Aktiv``
     - ``int32``
   * - ``InVariant``
     - ``boolean``
   * - ``Lfdnr``
     - ``int32``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``

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
     - Value Types
   * - ``Angle``
     - ``double``
   * - ``Beschreibung``
     - ``string``
   * - ``Dn``
     - ``single``
   * - ``Fkcont``
     - ``string``
   * - ``Fkkref``
     - ``string``
   * - ``Fkphi2``
     - ``string``
   * - ``Fkzep2``
     - ``string``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Iplanung``
     - ``int32``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``PositionOfDescription``
     - ``int32``
   * - ``ShowDescription``
     - ``boolean``
   * - ``SymbolFactor``
     - ``double``
   * - ``Tk``
     - ``string``
   * - ``Typ``
     - ``int32``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
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

SetpointDevice
^^^^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``Angle``
     - ``double``
   * - ``Beschreibung``
     - ``string``
   * - ``Fkcont``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Indwbg``
     - ``int32``
   * - ``Indwno``
     - ``int32``
   * - ``Ka``
     - ``string``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``RglSymbolTyp``
     - ``rglsymboltype``
   * - ``SymbolFactor``
     - ``double``
   * - ``Tk``
     - ``string``
   * - ``Wmax``
     - ``single``
   * - ``Wmin``
     - ``single``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.Fklfkt``
     - ``string``
   * - ``bz.Fkswvt``
     - ``string``
   * - ``bz.Indslw``
     - ``int32``
   * - ``bz.Slwkon``
     - ``single``

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

SolarCollector
^^^^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``A1``
     - ``single``
   * - ``A2``
     - ``single``
   * - ``Apertfl``
     - ``single``
   * - ``Beschreibung``
     - ``string``
   * - ``Bruttfl``
     - ``single``
   * - ``C1``
     - ``single``
   * - ``C2``
     - ``single``
   * - ``C3``
     - ``single``
   * - ``Ceff``
     - ``single``
   * - ``Eta0b``
     - ``single``
   * - ``Eta0hem``
     - ``single``
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
   * - ``InVariant``
     - ``boolean``
   * - ``Indfl``
     - ``int32``
   * - ``Indiam``
     - ``int32``
   * - ``Kthetad``
     - ``single``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Typ``
     - ``int32``

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
     - Value Types
   * - ``A``
     - ``single``
   * - ``Angle``
     - ``double``
   * - ``Beschreibung``
     - ``string``
   * - ``Dn``
     - ``single``
   * - ``Fkatab``
     - ``string``
   * - ``Fkcont``
     - ``string``
   * - ``Fkfstf``
     - ``string``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``Hb``
     - ``single``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Indatab``
     - ``int32``
   * - ``Iplanung``
     - ``int32``
   * - ``Knotk``
     - ``string``
   * - ``Mue``
     - ``single``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``SymbolFactor``
     - ``double``
   * - ``SymbolGraf``
     - ``symbol1c_graf``
   * - ``Tk``
     - ``string``
   * - ``U``
     - ``single``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``Zetaneg``
     - ``single``
   * - ``Zetapos``
     - ``single``
   * - ``Zkor``
     - ``single``
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

Street
^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Name``
     - ``string``
   * - ``Nummer``
     - ``string``
   * - ``Ort``
     - ``string``
   * - ``Ortsteil``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Tk``
     - ``string``

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
     - Value Types
   * - ``Angle``
     - ``double``
   * - ``Beschreibung``
     - ``string``
   * - ``E1``
     - ``string``
   * - ``E2``
     - ``string``
   * - ``Fkcont``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Indadd``
     - ``int32``
   * - ``Ka``
     - ``string``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``RglSymbolTyp``
     - ``rglsymboltype``
   * - ``SymbolFactor``
     - ``double``
   * - ``Tk``
     - ``string``
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

SwitchInBlock
^^^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``Beschreibung``
     - ``string``
   * - ``BoundingRectangle``
     - ``irectangle``
   * - ``ElementFont``
     - ``c3sfont``
   * - ``Fkblock``
     - ``string``
   * - ``Fkcont``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``TextColor``
     - ``color``
   * - ``Tk``
     - ``string``
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
     - Value Types
   * - ``Beschreibung``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Intpol``
     - ``int32``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Zeitoption``
     - ``int32``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``MAINELEMENT``
   * - ``T``

TemperatureTable_Row
^^^^^^^^^^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``Fk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``T``
     - ``single``
   * - ``Zeit``
     - ``single``
   * - ``Zeitstempel``
     - ``string``

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
     - Value Types
   * - ``Angle``
     - ``double``
   * - ``Beschreibung``
     - ``string``
   * - ``ElementColor``
     - ``color``
   * - ``ElementFont``
     - ``c3sfont``
   * - ``Fkcont``
     - ``string``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``Graftext``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Tk``
     - ``string``
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
     - Value Types
   * - ``Beschreibung``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Intpol``
     - ``int32``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Zeitoption``
     - ``int32``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``MAINELEMENT``
   * - ``W``

ThermalOutputTable_Row
^^^^^^^^^^^^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``Fk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``W``
     - ``single``
   * - ``Zeit``
     - ``single``
   * - ``Zeitstempel``
     - ``string``

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
     - Value Types
   * - ``Beschreibung``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Tk``
     - ``string``
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
     - Value Types
   * - ``Cp``
     - ``single``
   * - ``Fk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Lambda``
     - ``single``
   * - ``Name``
     - ``string``
   * - ``Nue``
     - ``single``
   * - ``Pd``
     - ``single``
   * - ``Pk``
     - ``string``
   * - ``Rho``
     - ``single``
   * - ``T``
     - ``single``

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
     - Value Types
   * - ``Angle``
     - ``double``
   * - ``Beschreibung``
     - ``string``
   * - ``Fkcont``
     - ``string``
   * - ``Idue``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``InputRues``
     - ``string``
   * - ``Iotyp``
     - ``int32``
   * - ``Ka``
     - ``string``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``RglSymbolTyp``
     - ``rglsymboltype``
   * - ``SymbolFactor``
     - ``double``
   * - ``Tk``
     - ``string``
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
     - Value Types
   * - ``Angle``
     - ``double``
   * - ``Beschreibung``
     - ``string``
   * - ``Fkcont``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Indaggreg``
     - ``int32``
   * - ``Indxbg``
     - ``int32``
   * - ``Indxno``
     - ``int32``
   * - ``Indxum``
     - ``int32``
   * - ``Ka``
     - ``string``
   * - ``Mesdt0``
     - ``single``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``RglSymbolTyp``
     - ``rglsymboltype``
   * - ``SymbolFactor``
     - ``double``
   * - ``Tk``
     - ``string``
   * - ``Xkor``
     - ``double``
   * - ``Xmax``
     - ``single``
   * - ``Xmin``
     - ``single``
   * - ``Xumb``
     - ``single``
   * - ``Xumm``
     - ``single``
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

TransportVariable
^^^^^^^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``InVariant``
     - ``boolean``
   * - ``Jchlorid``
     - ``int32``
   * - ``Jeisenfilt``
     - ``int32``
   * - ``Jeisenges``
     - ``int32``
   * - ``Jhi``
     - ``int32``
   * - ``Jhs``
     - ``int32``
   * - ``Jleitfaeh``
     - ``int32``
   * - ``Jmn``
     - ``int32``
   * - ``Jphwert``
     - ``int32``
   * - ``Jqualpar``
     - ``int32``
   * - ``Jrhon``
     - ``int32``
   * - ``Jsulfat``
     - ``int32``
   * - ``Jtemp``
     - ``int32``
   * - ``Jtrsptyp``
     - ``int32``
   * - ``Jwalter``
     - ``int32``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``

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
     - Value Types
   * - ``Description``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Name``
     - ``string``
   * - ``Objtype``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Valtype``
     - ``int32``

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
     - Value Types
   * - ``InVariant``
     - ``boolean``
   * - ``Lfdnr``
     - ``int32``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Showarrow``
     - ``int32``
   * - ``Tk``
     - ``string``

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
     - Value Types
   * - ``Attype``
     - ``string``
   * - ``Colormid``
     - ``int32``
   * - ``Csvpfad``
     - ``string``
   * - ``Cwend``
     - ``single``
   * - ``Cwmode``
     - ``int32``
   * - ``Cwstart``
     - ``single``
   * - ``Cwtype``
     - ``int32``
   * - ``Fk``
     - ``string``
   * - ``Iabsvalue``
     - ``int32``
   * - ``Icsvcolid``
     - ``int32``
   * - ``Icsvcolval``
     - ``int32``
   * - ``Icsvidprop``
     - ``string``
   * - ``Iinvert``
     - ``int32``
   * - ``InVariant``
     - ``boolean``
   * - ``Name``
     - ``string``
   * - ``Numcolor``
     - ``int32``
   * - ``Pk``
     - ``string``
   * - ``Prop``
     - ``string``
   * - ``Proptype``
     - ``int32``
   * - ``Reseletype``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Valueconst``
     - ``single``
   * - ``Valueend``
     - ``single``
   * - ``Valuelb``
     - ``single``
   * - ``Valuestart``
     - ``single``
   * - ``Valueub``
     - ``single``

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
     - Value Types
   * - ``InVariant``
     - ``boolean``
   * - ``Lfdnr``
     - ``int32``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``XLinks``
     - ``single``
   * - ``XRechts``
     - ``single``
   * - ``YOben``
     - ``single``
   * - ``YUnten``
     - ``single``

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
     - Value Types
   * - ``Angle``
     - ``double``
   * - ``Beschreibung``
     - ``string``
   * - ``Dn``
     - ``single``
   * - ``Fkcont``
     - ``string``
   * - ``Fkzep2``
     - ``string``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Indhub``
     - ``int32``
   * - ``Indzeta``
     - ``int32``
   * - ``IndzetaKlartext``
     - ``string``
   * - ``Iplanung``
     - ``int32``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``PositionOfDescription``
     - ``int32``
   * - ``ShowDescription``
     - ``boolean``
   * - ``SymbolFactor``
     - ``double``
   * - ``Thub``
     - ``single``
   * - ``Thub1``
     - ``single``
   * - ``Thub2``
     - ``single``
   * - ``Tk``
     - ``string``
   * - ``Tpaus``
     - ``single``
   * - ``Tsig``
     - ``single``
   * - ``Typ``
     - ``int32``
   * - ``TypKlartext``
     - ``string``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``Zetag``
     - ``single``
   * - ``Zetaneg``
     - ``single``
   * - ``Zetapos``
     - ``single``
   * - ``bz.Fk``
     - ``string``
   * - ``bz.Fkphi1``
     - ``string``
   * - ``bz.IndPhiKonst``
     - ``int32``
   * - ``bz.Indphi``
     - ``int32``
   * - ``bz.IndphiKlartext``
     - ``string``
   * - ``bz.Phig``
     - ``single``
   * - ``bz.Phio``
     - ``single``
   * - ``bz.Phisoll``
     - ``single``
   * - ``bz.Tiv``
     - ``single``

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

ValveLiftTable
^^^^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``Beschreibung``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Intpol``
     - ``int32``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Zeitoption``
     - ``int32``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``MAINELEMENT``
   * - ``PHI``

ValveLiftTable_Row
^^^^^^^^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``Fk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Name``
     - ``string``
   * - ``Phi``
     - ``single``
   * - ``Pk``
     - ``string``
   * - ``Zeit``
     - ``single``
   * - ``Zeitstempel``
     - ``string``

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
     - Value Types
   * - ``Beschreibung``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Intpol``
     - ``int32``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Zeitoption``
     - ``int32``

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

VarFlowTable_Row
^^^^^^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``Fk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Qm``
     - ``single``
   * - ``Zeit``
     - ``single``
   * - ``Zeitstempel``
     - ``string``

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
     - Value Types
   * - ``Beschreibung``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Intpol``
     - ``int32``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Zeitoption``
     - ``int32``

Result Properties
"""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Name
   * - ``MAINELEMENT``
   * - ``PH``

VarPressureTable_Row
^^^^^^^^^^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``Fk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Name``
     - ``string``
   * - ``Ph``
     - ``single``
   * - ``Pk``
     - ``string``
   * - ``Zeit``
     - ``single``
   * - ``Zeitstempel``
     - ``string``

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
     - Value Types
   * - ``Beschreibung``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Tk``
     - ``string``
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
     - Value Types
   * - ``Fk``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Name``
     - ``string``
   * - ``Phio``
     - ``single``
   * - ``Phis``
     - ``single``
   * - ``Pk``
     - ``string``
   * - ``Zeit``
     - ``single``

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
     - Value Types
   * - ``Alpha``
     - ``single``
   * - ``Angle``
     - ``double``
   * - ``Beschreibung``
     - ``string``
   * - ``Dgr``
     - ``single``
   * - ``Dkl``
     - ``single``
   * - ``Fkcont``
     - ``string``
   * - ``Fkfstf``
     - ``string``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``Ibedef``
     - ``int32``
   * - ``Ibetyp``
     - ``int32``
   * - ``Idreferenz``
     - ``string``
   * - ``Iekl``
     - ``int32``
   * - ``InVariant``
     - ``boolean``
   * - ``Iplanung``
     - ``int32``
   * - ``Knotk``
     - ``string``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Poeff``
     - ``single``
   * - ``Qlbmax``
     - ``single``
   * - ``Qlekl``
     - ``single``
   * - ``Rgbeve``
     - ``single``
   * - ``SymbolFactor``
     - ``double``
   * - ``SymbolGraf``
     - ``symbol1c_graf``
   * - ``Tk``
     - ``string``
   * - ``Trohr``
     - ``single``
   * - ``Vgrest``
     - ``single``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``Zkor``
     - ``single``
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

VentilatedPressureAirVessel
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``A``
     - ``single``
   * - ``Angle``
     - ``double``
   * - ``Beschreibung``
     - ``string``
   * - ``Dn``
     - ``single``
   * - ``Fkatab``
     - ``string``
   * - ``Fkcont``
     - ``string``
   * - ``Fkfstf``
     - ``string``
   * - ``GeometriesDiffer``
     - ``boolean``
   * - ``Hb``
     - ``single``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Indatab``
     - ``int32``
   * - ``Iplanung``
     - ``int32``
   * - ``Knotk``
     - ``string``
   * - ``Lta``
     - ``single``
   * - ``Name``
     - ``string``
   * - ``Pg0``
     - ``single``
   * - ``Pk``
     - ``string``
   * - ``Rgas``
     - ``single``
   * - ``Rpoly``
     - ``single``
   * - ``SymbolFactor``
     - ``double``
   * - ``SymbolGraf``
     - ``symbol1c_graf``
   * - ``Tgas``
     - ``single``
   * - ``Tk``
     - ``string``
   * - ``Xkor``
     - ``double``
   * - ``Ykor``
     - ``double``
   * - ``Zetaneg``
     - ``single``
   * - ``Zetapos``
     - ``single``
   * - ``Zkor``
     - ``single``
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

WBLZ_ThermalBalance
^^^^^^^^^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``Aktiv``
     - ``int32``
   * - ``Beschreibung``
     - ``string``
   * - ``Idim``
     - ``int32``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Name``
     - ``string``
   * - ``ObjsString``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Tk``
     - ``string``
   * - ``Typ``
     - ``string``

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

WeatherDataTable
^^^^^^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``Albedo``
     - ``single``
   * - ``Beschreibung``
     - ``string``
   * - ``Idreferenz``
     - ``string``
   * - ``InVariant``
     - ``boolean``
   * - ``Intpol``
     - ``int32``
   * - ``Lat``
     - ``single``
   * - ``Lon``
     - ``single``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Stdlon``
     - ``single``
   * - ``Zeitoption``
     - ``int32``

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

WeatherDataTable_Row
^^^^^^^^^^^^^^^^^^^^

Properties
""""""""""

.. list-table::
   :header-rows: 1

   * - Name
     - Value Types
   * - ``Fk``
     - ``string``
   * - ``Gdiff``
     - ``single``
   * - ``Gglob``
     - ``single``
   * - ``InVariant``
     - ``boolean``
   * - ``Name``
     - ``string``
   * - ``Pk``
     - ``string``
   * - ``Temp``
     - ``single``
   * - ``Wind``
     - ``single``
   * - ``Zeit``
     - ``single``
   * - ``Zeitstempel``
     - ``string``

Result Properties
"""""""""""""""""

No result properties found.

