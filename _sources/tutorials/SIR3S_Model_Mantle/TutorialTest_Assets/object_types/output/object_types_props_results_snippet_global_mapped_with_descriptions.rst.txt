Object Types, Properties, and Result Value Types
---------------------------------------------

.. note:: Aggregated global view across configured network types.
   The below sections lists all table names from self.ObjectTypes_TableNames, along with their properties, result properties, and respective object type from self.ObjectTypes (needed for toolkit operations like self.InsertElement(), self.GetPropertiesOfElementType()).
   Result properties additionally list a Description and Standard Physical Unit where known, sourced from SIR 3S's own .MX1 output plus a handful of manual additions (see result_props_descriptions.ipynb). Both are in German, as embedded in SIR 3S itself.

AGSN
^^^^
Object Type: ``AGSN_HydraulicProfile``


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

ALLG
^^^^
Object Type: ``GeneralSection``


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
     - Description
     - Standard Physical Unit
   * - ``CPUTIME``
     - ``CPU-Zeit seit Start``
     - ``[s]``
   * - ``CVERSO``
     - ``Versionskennung``
     - ``[text]``
   * - ``EXSTAT``
     - ``Exit-Status der Berechnung``
     - ``[]``
   * - ``FWVB_DPHMIN``
     - ``Min. Differenzdruck aller Verbraucher``
     - ``[bar]``
   * - ``FWVB_TVLMIN``
     - ``Min. VL-Temperatur aller Verbraucher``
     - ``[°C]``
   * - ``INTERAKTRG``
     - ``Anzahl benötigter Sign.-Durchläufe``
     - ``[]``
   * - ``INTERAKTTH``
     - ``Anzahl benötigter therm. Durchläufe``
     - ``[]``
   * - ``ITERHY``
     - ``Anzahl benötigter hydr. Iterationen``
     - ``[]``
   * - ``ITERTH``
     - ``Anzahl benötigter therm. Iterationen``
     - ``[]``
   * - ``JWARN``
     - ``Warnstufe``
     - ``[]``
   * - ``KNOT_PHMAX``
     - ``Max. Knotendruck im Netz``
     - ``[bar]``
   * - ``KNOT_PHMAX_R``
     - ``Max. Knotendruck im Netz RL``
     - ``[bar]``
   * - ``KNOT_PHMAX_U``
     - ``Max. Knotendruck im Netz undef.``
     - ``[bar]``
   * - ``KNOT_PHMAX_V``
     - ``Max. Knotendruck im Netz VL``
     - ``[bar]``
   * - ``KNOT_PHMIN``
     - ``Min. Knotendruck im Netz``
     - ``[bar]``
   * - ``KNOT_PHMIN_R``
     - ``Min. Knotendruck im Netz RL``
     - ``[bar]``
   * - ``KNOT_PHMIN_U``
     - ``Min. Knotendruck im Netz undef.``
     - ``[bar]``
   * - ``KNOT_PHMIN_V``
     - ``Min. Knotendruck im Netz VL``
     - ``[bar]``
   * - ``LFQSV``
     - ``Lastfaktor für Strangentnahmen``
     - ``[]``
   * - ``LINEPACKGEOM``
     - ``Gesamt-Linepack Rohrinhalt``
     - ``[(N)m3]``
   * - ``LINEPACKGES``
     - ``Gesamt-Linepack``
     - ``[(N)m3]``
   * - ``LINEPACKRATE``
     - ``Gesamt-Linepack-Rate``
     - ``[(N)m3/h]``
   * - ``MAINELEMENT``
     - 
     - 
   * - ``MFVHYUV``
     - ``Fehlmenge FWVB aus hydr. Unterversorgung``
     - ``[m3/h]``
   * - ``MFVTHUV``
     - ``Fehlmenge FWVB aus ther. Unterversorgung``
     - ``[m3/h]``
   * - ``MKNUV``
     - ``Fehlmenge KNOT aus Unterversorgung``
     - ``[m3/h]``
   * - ``NETZABN``
     - ``Netzabnahme``
     - ``[m3/h]``
   * - ``NETZABNEXITS``
     - ``Netzabnahme ohne Druckränder``
     - ``[m3/h]``
   * - ``NETZBEZ``
     - ``Netzbezug``
     - ``[m3/h]``
   * - ``NFEHL``
     - ``Anzahl Fehler im Berechnungsabschnitt``
     - ``[]``
   * - ``NFVHYUV``
     - ``Anzahl FWVB mit hydr. Unterversorgung``
     - ``[]``
   * - ``NFVTHUV``
     - ``Anzahl FWVB mit ther. Unterversorgung``
     - ``[]``
   * - ``NKNUV``
     - ``Anzahl KNOT mit Unterversorgung``
     - ``[]``
   * - ``NMELD``
     - ``Anzahl Meldungen im Berechnungsabschnitt``
     - ``[]``
   * - ``NPGREST``
     - ``Anzahl aktiver PGRP in Restriktion``
     - ``[]``
   * - ``NWARN``
     - ``Anzahl Warnungen im Berechnungsabschnitt``
     - ``[]``
   * - ``PAV``
     - ``Mittlerer Druck``
     - ``[bar,a]``
   * - ``RHOAV``
     - ``Mittlere Dichte``
     - ``[kg/m3]``
   * - ``SNAPSHOTTYPE``
     - ``Typ des Zeitpunktes/Ausgabedatensatzes``
     - ``[text]``
   * - ``TAV``
     - ``Mittlere Temperatur``
     - ``[°C]``
   * - ``TIMESTAMP``
     - ``Zeitstempel nach ISO 8601``
     - ``[text]``
   * - ``TVMINMAX``
     - ``Maximum der erf. min. VL-Temperatur``
     - ``[°C]``
   * - ``USRTIME``
     - ``USR-Zeit seit Start``
     - ``[s]``

ANTP
^^^^
Object Type: ``DrivePowerTable``


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

ANTP_ROWS
^^^^^^^^^
Object Type: ``DrivePowerTable_Row``


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

ARRW
^^^^
Object Type: ``Arrow``


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

ATMO
^^^^
Object Type: ``Atmosphere``


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

AVOS
^^^^
Object Type: ``CrossSectionTable``


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

AVOS_ROWS
^^^^^^^^^
Object Type: ``CrossSectionTable_Row``


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

BEVE
^^^^
Object Type: ``VentValve``


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
     - Description
     - Standard Physical Unit
   * - ``IAKTIV``
     - ``Netztrennstatus``
     - ``[]``
   * - ``IND``
     - ``Betriebszustand``
     - ``[]``
   * - ``M``
     - ``Fluidmassenstrom``
     - ``[kg/s]``
   * - ``MAINELEMENT``
     - 
     - 
   * - ``MLUFT``
     - ``Luftmassenstrom``
     - ``[kg/s]``
   * - ``PHI``
     - ``Querschnitt Be- und Entlüftung``
     - ``[%]``
   * - ``PLUFT``
     - ``Druck im Luftvolumen``
     - ``[bar,a]``
   * - ``QLUFT``
     - ``Luftvolumenstrom``
     - ``[m3/s]``
   * - ``QM``
     - ``Durchfluss``
     - ``[m3/h]``
   * - ``QMLUFT``
     - ``Luftstrom``
     - ``[m3/h]``
   * - ``RHO``
     - ``Dichte``
     - ``[kg/m3]``
   * - ``TLUFT``
     - ``Lufttemperatur``
     - ``[°C]``
   * - ``VLUFT``
     - ``Strömungsgeschwindigkeit Luft``
     - ``[m/s]``
   * - ``VOLLUFT``
     - ``Luftvolumen``
     - ``[m3]``

BEWI
^^^^
Object Type: ``VentilatedPressureAirVessel``


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
     - Description
     - Standard Physical Unit
   * - ``HLUFT``
     - ``Druckhöhe im Luftvolumen``
     - ``[mNN]``
   * - ``IAKTIV``
     - ``Netztrennstatus``
     - ``[]``
   * - ``IND``
     - ``Betriebszustand``
     - ``[]``
   * - ``M``
     - ``Massenstrom``
     - ``[kg/s]``
   * - ``MAINELEMENT``
     - 
     - 
   * - ``PLUFT``
     - ``Druck im Luftvolumen``
     - ``[bar,a]``
   * - ``QM``
     - ``Durchfluss``
     - ``[m3/h]``
   * - ``RHO``
     - ``Dichte``
     - ``[kg/m3]``
   * - ``T``
     - ``Fluidtemperatur``
     - ``[°C]``
   * - ``TLUFT``
     - ``Temperatur im Luftvolumen``
     - ``[°C]``
   * - ``V``
     - ``Strömungsgeschwindigkeit Anschluss``
     - ``[m/s]``
   * - ``VOL``
     - ``Wasservolumen``
     - ``[m3]``
   * - ``VOLLUFT``
     - ``Luftvolumen``
     - ``[m3]``
   * - ``VOLLUFT1``
     - ``Luftvolumen unter Tauchrohr``
     - ``[m3]``
   * - ``WALTER``
     - ``Wasseralter``
     - ``[h]``
   * - ``WST``
     - ``Wasserstand``
     - ``[m]``

BREF
^^^^
Object Type: ``SwitchInBlock``


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

CIRC
^^^^
Object Type: ``Circle``


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

CONT
^^^^
Object Type: ``ObjectContainerSymbol``


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

CRGL
^^^^
Object Type: ``ControlEngineeringNexus``


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

DPGR
^^^^
Object Type: ``DPGR_DataPointGroup``


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

DPGR_DPKT
^^^^^^^^^
Object Type: ``DPGR_DPKT_DatapointDpgrConnection``


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

DPKT
^^^^
Object Type: ``DPKT_Datapoint``


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

DPRG
^^^^
Object Type: ``DifferentialRegulator``


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
     - Description
     - Standard Physical Unit
   * - ``DH``
     - ``Differenzdruckhöhe``
     - ``[m]``
   * - ``DP``
     - ``Differenzdruck``
     - ``[bar]``
   * - ``DPH``
     - ``Reibungsdruckverlust/-druckverlusthöhe``
     - ``[bar]``
   * - ``DPHSOLL``
     - ``Sollwert Differenzdruck/-druckhöhe``
     - ``[bar]``
   * - ``DPSOLL``
     - ``Sollwert Differenzdruck``
     - ``[bar]``
   * - ``DSI``
     - ``dynamische Stützkraft Knoten I``
     - ``[N|kN|MN]``
   * - ``DSK``
     - ``dynamische Stützkraft Knoten K``
     - ``[N|kN|MN]``
   * - ``FS``
     - ``dynamische axiale Last``
     - ``[N|kN|MN]``
   * - ``HR``
     - ``Reibungsdruckverlusthöhe``
     - ``[m]``
   * - ``IAKTIV``
     - ``Netztrennstatus``
     - ``[]``
   * - ``KV``
     - ``KV-Wert``
     - ``[m3/h]``
   * - ``M``
     - ``Massenstrom``
     - ``[kg/s]``
   * - ``MAINELEMENT``
     - 
     - 
   * - ``PHI``
     - ``Reglerstellung``
     - ``[%]``
   * - ``PR``
     - ``Reibungsdruckverlust``
     - ``[bar]``
   * - ``QM``
     - ``Durchfluss``
     - ``[m3/h]``
   * - ``RHO``
     - ``Dichte``
     - ``[kg/m3]``
   * - ``SWVT``
     - ``Name Sollwerttabelle``
     - ``[3Sname]``
   * - ``V``
     - ``Strömungsgeschwindigkeit``
     - ``[m/s]``
   * - ``ZETA``
     - ``Verlustbeiwert, berechnet``
     - ``[]``

DTRO
^^^^
Object Type: ``PipeTable``


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

DTRO_ROWD
^^^^^^^^^
Object Type: ``PipeTable_Row``


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

EBES
^^^^
Object Type: ``EBES_FeederGroups``


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

ELEMENTQUERY
^^^^^^^^^^^^
Object Type: ``ElementQuery``


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

ERROR_NO_MAPPING__RART_ControlMode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Object Type: ``RART_ControlMode``


Properties
""""""""""

No properties found.

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

ERROR_NO_MAPPING__Unknown
^^^^^^^^^^^^^^^^^^^^^^^^^
Object Type: ``Unknown``


Properties
""""""""""

No properties found.

Result Properties
"""""""""""""""""

No result properties found.

ETAM
^^^^
Object Type: ``DriveEfficiencyTable``


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

ETAM_ROWS
^^^^^^^^^
Object Type: ``DriveEfficiencyTable_Row``


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

ETAR
^^^^
Object Type: ``EnergyRecoveryTable``


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

ETAR_ROWS
^^^^^^^^^
Object Type: ``EnergyRecoveryTable_Row``


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

ETAU
^^^^
Object Type: ``EfficiencyConverterTable``


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

ETAU_ROWS
^^^^^^^^^
Object Type: ``EfficiencyConverterTable_Row``


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

FKNL
^^^^
Object Type: ``FreeDuct``


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
     - Description
     - Standard Physical Unit
   * - ``MAINELEMENT``
     - 
     - 
   * - ``OA``
     - ``Obere Alarmgrenze überschritten``
     - ``[]``
   * - ``OW``
     - ``Obere Warngrenze überschritten``
     - ``[]``
   * - ``UA``
     - ``Untere Alarmgrenze unterschritten``
     - ``[]``
   * - ``UW``
     - ``Untere Warngrenze unterschritten``
     - ``[]``
   * - ``WERT``
     - ``Sollwert``
     - ``[unitX]``

FQPS
^^^^
Object Type: ``FluidQualityParamSet``


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
     - Description
     - Standard Physical Unit
   * - ``MAINELEMENT``
     - 
     - 
   * - ``SWVTCHLORID``
     - ``Name Sollwerttabelle Chlorid``
     - ``[3Sname]``
   * - ``SWVTEISENFILT``
     - 
     - 
   * - ``SWVTEISENGES``
     - ``Name Sollwerttabelle Eisengehalt gesamt``
     - ``[3Sname]``
   * - ``SWVTHI``
     - ``Name Sollwerttabelle Heizwert``
     - ``[3Sname]``
   * - ``SWVTHS``
     - ``Name Sollwerttabelle Brennwert``
     - ``[3Sname]``
   * - ``SWVTLEITFAEH``
     - ``Name Sollwerttabelle Leitfähigkeit``
     - ``[3Sname]``
   * - ``SWVTMN``
     - ``Name Sollwerttabelle Methanzahl``
     - ``[3Sname]``
   * - ``SWVTPHWERT``
     - ``Name Sollwerttabelle PH-Wert``
     - ``[3Sname]``
   * - ``SWVTRHON``
     - ``Name Sollwerttabelle Normdichte``
     - ``[3Sname]``
   * - ``SWVTSULFAT``
     - ``Name Sollwerttabelle Sulfat``
     - ``[3Sname]``
   * - ``SWVTTEMP``
     - ``Name Sollwerttabelle Temperatur``
     - ``[3Sname]``

FQPS_BZ
^^^^^^^
Object Type: ``FluidQualityParamSet_OS``


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

FSTF
^^^^
Object Type: ``FluidThermalPropertyGroup``


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

FWBZ
^^^^
Object Type: ``FWBZ_DistrictHeatingReferenceValues``


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

FWEA
^^^^
Object Type: ``HeatFeederConsumerStation``


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
     - Description
     - Standard Physical Unit
   * - ``DH_KALT``
     - 
     - 
   * - ``DH_MIX``
     - 
     - 
   * - ``DH_WARM``
     - 
     - 
   * - ``DPH_ES``
     - ``Differenzdruck Einspeiser``
     - ``[bar]``
   * - ``DPH_VB``
     - ``Differenzdruck Abnehmer``
     - ``[bar]``
   * - ``DTLEER``
     - 
     - 
   * - ``ETA_PU``
     - ``Wirkungsgrad Einspeisepumpe``
     - ``[]``
   * - ``GGLOB``
     - ``Globalstrahlung``
     - ``[W/m²]``
   * - ``GKOLL``
     - ``Strahlung auf Kollektorebene``
     - ``[W/m²]``
   * - ``H_MIX``
     - 
     - 
   * - ``H_PU``
     - ``Förderhöhe Einspeisepumpe``
     - ``[m]``
   * - ``H_WS``
     - ``FreeTTES: Wasserstand``
     - ``[m]``
   * - ``IAKTIV``
     - ``Netztrennstatus``
     - ``[]``
   * - ``MAINELEMENT``
     - 
     - 
   * - ``MMAXBL``
     - 
     - 
   * - ``MMAXEL``
     - 
     - 
   * - ``MMIN``
     - 
     - 
   * - ``N_PU``
     - ``Drehzahl Einspeisepumpe``
     - ``[1/min]``
   * - ``P_PU``
     - ``Hydraulische Leistung Einspeisepumpe``
     - ``[kW]``
   * - ``QM``
     - ``Durchfluss zum Netz``
     - ``[t/h]``
   * - ``QM_ES``
     - ``Durchfluss Einspeiser/Pumpe``
     - ``[t/h]``
   * - ``QM_PR``
     - ``Durchfluss Überströmer``
     - ``[t/h]``
   * - ``QM_VB``
     - ``Durchfluss Abnehmer``
     - ``[t/h]``
   * - ``QSP``
     - ``Wärmeinhalt``
     - ``[kWh]``
   * - ``QSPREL``
     - ``Relativer Wärmeinhalt``
     - ``[%]``
   * - ``QV_BODEN``
     - 
     - 
   * - ``QV_DR``
     - ``FreeTTES: Wärmegewinn Dampfraum``
     - ``[kW]``
   * - ``QV_MANTEL``
     - 
     - 
   * - ``QV_TOTAL``
     - 
     - 
   * - ``Q_PU``
     - ``Volumenstrom Einspeisepumpe``
     - ``[m³/h]``
   * - ``TDIFFO``
     - 
     - 
   * - ``TDIFFU``
     - 
     - 
   * - ``TRL``
     - ``Rücklauftemperatur``
     - ``[°C]``
   * - ``TRS``
     - ``Rückspeisetemperatur``
     - ``[°C]``
   * - ``TSP``
     - ``Speisetemperatur``
     - ``[°C]``
   * - ``TVEC``
     - ``FreeTTES Speichergitter: Temp.-Profil``
     - ``[°C]``
   * - ``TVL``
     - ``Vorlauftemperatur``
     - ``[°C]``
   * - ``T_KALT``
     - 
     - 
   * - ``T_MIX``
     - 
     - 
   * - ``T_WARM``
     - 
     - 
   * - ``W``
     - ``Wärmeleistung zum Netz``
     - ``[kW]``
   * - ``WKOLL``
     - ``Strahlungsleistung auf Kollektorfläche``
     - ``[kW]``
   * - ``W_ES``
     - ``Wärmeleistung Einspeiser``
     - ``[kW]``
   * - ``W_FS``
     - ``Wärmeleistung Frostschutz``
     - ``[kW]``
   * - ``W_PR``
     - ``Überschüssige Wärmeleistung``
     - ``[kW]``
   * - ``W_RO``
     - ``Wärmeverlustleistung Rohrleitungen``
     - ``[kW]``
   * - ``W_VB``
     - ``Wärmeleistung Abnehmer``
     - ``[kW]``

FWES
^^^^
Object Type: ``DistrictHeatingFeeder``


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
     - Description
     - Standard Physical Unit
   * - ``DH``
     - ``Differenzdruckhöhe``
     - ``[m]``
   * - ``DP``
     - ``Differenzdruck``
     - ``[bar]``
   * - ``DPH``
     - ``Reibungsdruckverlust/-druckverlusthöhe``
     - ``[bar]``
   * - ``IAKTIV``
     - ``Netztrennstatus``
     - ``[]``
   * - ``IHYTYP``
     - ``Hydraulische Fahrweise``
     - ``[]``
   * - ``ITHTYP``
     - ``Thermische Fahrweise``
     - ``[]``
   * - ``M``
     - ``Massenstrom``
     - ``[kg/s]``
   * - ``MAINELEMENT``
     - 
     - 
   * - ``QM``
     - ``Durchfluss``
     - ``[t/h]``
   * - ``RHOI``
     - ``Zulaufdichte``
     - ``[kg/m3]``
   * - ``RHOK``
     - ``Speisedichte``
     - ``[kg/m3]``
   * - ``TEVT``
     - ``Name Zeittabelle Speisetemperatur``
     - ``[3Sname]``
   * - ``TI``
     - ``Zulauftemperatur``
     - ``[°C]``
   * - ``TK``
     - ``Speisetemperatur``
     - ``[°C]``
   * - ``TKON``
     - ``Konstante Speisetemperatur``
     - ``[°C]``
   * - ``V``
     - ``Strömungsgeschwindigkeit``
     - ``[m/s]``
   * - ``W``
     - ``Wärmeleistung``
     - ``[kW]``
   * - ``W0``
     - ``Wärmeleistung konstant``
     - ``[kW]``
   * - ``WEVT``
     - ``Name Zeittabelle Wärmeleistung``
     - ``[3Sname]``
   * - ``WSOLL``
     - ``Sollwert Wärmeleistung``
     - ``[kW]``

FWVB
^^^^
Object Type: ``DistrictHeatingConsumer``


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
     - Description
     - Standard Physical Unit
   * - ``DH``
     - ``Differenzdruckhöhe``
     - ``[m]``
   * - ``DP``
     - ``Differenzdruck``
     - ``[bar]``
   * - ``DPH``
     - ``Reibungsdruckverlust/-druckverlusthöhe``
     - ``[bar]``
   * - ``IAKTIV``
     - ``Netztrennstatus``
     - ``[]``
   * - ``INDUV``
     - ``Indikator Unterversorgung``
     - ``[]``
   * - ``LFH``
     - ``Hydraulischer Lastfaktor``
     - ``[]``
   * - ``LFKT``
     - ``Name Lastgangtabelle``
     - ``[3Sname]``
   * - ``LFT``
     - ``Thermischer Lastfaktor``
     - ``[]``
   * - ``M``
     - ``Massenstrom``
     - ``[kg/s]``
   * - ``MAINELEMENT``
     - 
     - 
   * - ``MHYUV``
     - ``Mengendefizit aus hydr. Unterversorgung``
     - ``[t/h]``
   * - ``MSOLL``
     - ``Sollmassenstrom``
     - ``[kg/s]``
   * - ``MTHUV``
     - ``Mengendefizit aus therm. Unterversorgung``
     - ``[t/h]``
   * - ``P1``
     - ``Druck hinter VL Armatur``
     - ``[bar]``
   * - ``P2``
     - ``Druck vor RL Armatur``
     - ``[bar]``
   * - ``P3``
     - ``Druck am kompressiblen Volumen``
     - ``[bar]``
   * - ``PH1``
     - ``Druck hinter VL Armatur``
     - ``[bar]``
   * - ``PH2``
     - ``Druck vor RL Armatur``
     - ``[bar]``
   * - ``PH3``
     - ``Druck am kompressiblen Volumen``
     - ``[bar]``
   * - ``PHIRL``
     - ``Stellung RL Armatur``
     - ``[%]``
   * - ``PHIVL``
     - ``Stellung VL Armatur``
     - ``[%]``
   * - ``QM``
     - ``Durchfluss``
     - ``[t/h]``
   * - ``QM13``
     - ``Abzw. Durchfl. in Richtung kompress. Vol``
     - ``[t/h]``
   * - ``QM31``
     - ``Zulaufdurchfluss kompressibles Volumen``
     - ``[t/h]``
   * - ``QMI``
     - ``Durchfluss Vorlauf``
     - ``[t/h]``
   * - ``QMK``
     - ``Durchfluss Rücklauf``
     - ``[t/h]``
   * - ``QVAR``
     - ``Name Zeittabelle Durchfluss``
     - ``[3Sname]``
   * - ``RHOI``
     - ``Dichte Vorlauf``
     - ``[kg/m3]``
   * - ``RHOK``
     - ``Dichte Rücklauf``
     - ``[kg/m3]``
   * - ``TI``
     - ``Vorlauftemperatur``
     - ``[°C]``
   * - ``TK``
     - ``Rückspeisetemperatur``
     - ``[°C]``
   * - ``TVMIN``
     - ``Minimale Vorlauftemperatur``
     - ``[]``
   * - ``W``
     - ``Wärmeleistung``
     - ``[kW]``
   * - ``WHYUV``
     - ``Wärmedefizit aus hydr. Unterversorgung``
     - ``[kW]``
   * - ``WSOLL``
     - ``Sollwert Wärmeleistung``
     - ``[kW]``
   * - ``WTHUV``
     - ``Wärmedefizit aus therm. Unterversorgung``
     - ``[kW]``

FWWU
^^^^
Object Type: ``HeatExchanger``


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
     - Description
     - Standard Physical Unit
   * - ``AKTIV``
     - ``Aktivitätszustand``
     - ``[]``
   * - ``C1``
     - ``Verhältnis Wärmekapazitätsströme W1/W2``
     - ``[]``
   * - ``C2``
     - ``Verhältnis Wärmekapazitätsströme W2/W1``
     - ``[]``
   * - ``EPS1``
     - ``Temperaturänderung primär``
     - ``[]``
   * - ``EPS2``
     - ``Temperaturänderung sekundär``
     - ``[]``
   * - ``IAKTIV``
     - ``Netztrennstatus``
     - ``[]``
   * - ``INDUV``
     - ``Indikator Unterversorgung``
     - ``[]``
   * - ``KA``
     - ``Übertragungsfähigkeit``
     - ``[kW/K]``
   * - ``MAINELEMENT``
     - 
     - 
   * - ``NTU1``
     - ``Übertragungsfähigkeit (NTU) primär``
     - ``[]``
   * - ``NTU2``
     - ``Übertragungsfähigkeit (NTU) sekundär``
     - ``[]``
   * - ``NU1``
     - ``Nußelt-Zahl primär``
     - ``[]``
   * - ``NU2``
     - ``Nußelt-Zahl sekundär``
     - ``[]``
   * - ``PR1``
     - ``Prandtl-Zahl primär``
     - ``[]``
   * - ``PR2``
     - ``Prandtl-Zahl sekundär``
     - ``[]``
   * - ``Q``
     - ``Übertragungsleistung``
     - ``[kW]``
   * - ``RE1``
     - ``Reynolds-Zahl primär``
     - ``[]``
   * - ``RE2``
     - ``Reynolds-Zahl sekundär``
     - ``[]``
   * - ``T1AUS``
     - ``Austrittstemperatur primär``
     - ``[°C]``
   * - ``T1EIN``
     - ``Eintrittstemperatur primär``
     - ``[°C]``
   * - ``T2AUS``
     - ``Austrittstemperatur sekundär``
     - ``[°C]``
   * - ``T2EIN``
     - ``Eintrittstemperatur sekundär``
     - ``[°C]``
   * - ``THETA``
     - ``Dimensionslose mittlere Temperaturdiff.``
     - ``[]``
   * - ``TMLOG``
     - ``Mittlere Temperaturdifferenz``
     - ``[K]``
   * - ``W1``
     - ``Wärmekapazitätsstrom primär``
     - ``[kJ/(s K)]``
   * - ``W2``
     - ``Wärmekapazitätsstrom sekundär``
     - ``[kJ/(s K)]``

GKMP
^^^^
Object Type: ``GasComponent``


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

GMIX
^^^^
Object Type: ``GasMixture``


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

GRAV
^^^^
Object Type: ``Gravitation``


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

GTXT
^^^^
Object Type: ``Text``


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

GVWK
^^^^
Object Type: ``HeaterCooler``


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
     - Description
     - Standard Physical Unit
   * - ``EINAUS``
     - ``Heizer/Kühler ein/aus``
     - ``[]``
   * - ``IAKTIV``
     - ``Netztrennstatus``
     - ``[]``
   * - ``M``
     - ``Massenstrom``
     - ``[kg/s]``
   * - ``MAINELEMENT``
     - 
     - 
   * - ``P``
     - ``Leistung``
     - ``[kW]``
   * - ``PE``
     - ``Energieverbrauch``
     - ``[kW]``
   * - ``PI``
     - ``Eingangsdruck``
     - ``[bar]``
   * - ``PK``
     - ``Ausgangsdruck``
     - ``[bar]``
   * - ``QN``
     - ``Durchfluss``
     - ``[Nm3/h]``
   * - ``TI``
     - ``Eingangstemperatur``
     - ``[°C]``
   * - ``TK``
     - ``Ausgangstemperatur``
     - ``[°C]``

HAUS
^^^^
Object Type: ``House``


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

HYDR
^^^^
Object Type: ``Hydrant``


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
     - Description
     - Standard Physical Unit
   * - ``BCTYP``
     - ``Verhalten, Funktion, Bedingung``
     - ``[]``
   * - ``IAKTIV``
     - ``Aktivität``
     - ``[]``
   * - ``MAINELEMENT``
     - 
     - 
   * - ``PHR``
     - ``Reibungsdruckverlust Hydrant``
     - ``[bar]``
   * - ``PHR_ROHR``
     - ``Reibungsdruckverlust Anschlussleitung``
     - ``[bar]``
   * - ``PHSOLL``
     - ``Solldruck am Einbindepunkt``
     - ``[bar]``
   * - ``PH_EINB``
     - ``Druck am Einbindepunkt``
     - ``[bar]``
   * - ``PH_ENTN``
     - ``Druck am Entnahmepunkt``
     - ``[bar]``
   * - ``PH_MIN``
     - ``Mindest- oder Solldruck am Entnahmepunkt``
     - ``[bar]``
   * - ``QM``
     - ``Entnahmemenge``
     - ``[m3/h]``
   * - ``QSOLL``
     - ``Sollentnahmemenge``
     - ``[m3/h]``
   * - ``UV``
     - ``Entnahmeleistung``
     - ``[%]``

KLAP
^^^^
Object Type: ``FlapValve``


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
     - Description
     - Standard Physical Unit
   * - ``DH``
     - ``Differenzdruckhöhe``
     - ``[m]``
   * - ``DP``
     - ``Differenzdruck``
     - ``[bar]``
   * - ``DSI``
     - ``dynamische Stützkraft Knoten I``
     - ``[N|kN|MN]``
   * - ``DSK``
     - ``dynamische Stützkraft Knoten K``
     - ``[N|kN|MN]``
   * - ``FS``
     - ``dynamische axiale Last``
     - ``[N|kN|MN]``
   * - ``HR``
     - ``Reibungsdruckverlusthöhe``
     - ``[m]``
   * - ``IAKTIV``
     - ``Netztrennstatus``
     - ``[]``
   * - ``KV``
     - ``KV-Wert``
     - ``[m3/h]``
   * - ``M``
     - ``Massenstrom``
     - ``[kg/s]``
   * - ``MAINELEMENT``
     - 
     - 
   * - ``PHI``
     - ``Stellung``
     - ``[%]``
   * - ``PHR``
     - ``Reibungsdruckverlust/-druckverlusthöhe``
     - ``[bar]``
   * - ``PR``
     - ``Reibungsdruckverlust``
     - ``[bar]``
   * - ``QM``
     - ``Durchfluss``
     - ``[m3/h]``
   * - ``RHO``
     - ``Dichte``
     - ``[kg/m3]``
   * - ``V``
     - ``Strömungsgeschwindigkeit``
     - ``[m/s]``
   * - ``ZETA``
     - ``Verlustbeiwert``
     - ``[]``

KNOT
^^^^
Object Type: ``Node``


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
     - Description
     - Standard Physical Unit
   * - ``BCIND``
     - ``Indikator Rand (Summencode)``
     - ``[]``
   * - ``BCIND_CALC``
     - ``Indikator Rand Berechnet``
     - ``[]``
   * - ``BCIND_FLOW``
     - ``Indikator Rand Durchfluss``
     - ``[]``
   * - ``BCIND_MODEL``
     - ``Indikator Rand Modelliert``
     - ``[]``
   * - ``BCIND_SOURCE``
     - ``Indikator Rand Herkunft``
     - ``[]``
   * - ``BCIND_TYPE``
     - ``Indikator Rand Typ``
     - ``[]``
   * - ``CHLORID``
     - ``Chlorid``
     - ``[mg/l]``
   * - ``CP``
     - ``Spezifische Wärmekapazität``
     - ``[kJ/kg/K]``
   * - ``DP``
     - ``Differenzdruck zwischen VL und RL``
     - ``[bar]``
   * - ``DPH``
     - ``Differenzdruck zwischen VL und RL``
     - ``[bar]``
   * - ``DYNVISKO``
     - ``Dynamische Viskosität``
     - ``[kg/m/s]``
   * - ``EH``
     - ``Energiehöhe``
     - ``[mNN]``
   * - ``EISENFILT``
     - ``Eisengehalt im Filtrat``
     - ``[mg/l]``
   * - ``EISENGES``
     - ``Eisengehalt gesamt``
     - ``[mg/l]``
   * - ``ESQUELLSP``
     - ``Einspeiserquellspektrum``
     - ``[%]``
   * - ``FITT_ANGLE``
     - ``Formstück: Winkel``
     - ``[°]``
   * - ``FITT_BASTYPE``
     - ``Formstück: Typ``
     - ``[]``
   * - ``FITT_DP1``
     - ``Formstück: Druckverlust am VBEL1``
     - ``[bar]``
   * - ``FITT_DP2``
     - ``Formstück: Druckverlust am VBEL 2``
     - ``[bar]``
   * - ``FITT_DP3``
     - ``Formstück: Druckverlust am VBEL 3``
     - ``[bar]``
   * - ``FITT_STATE``
     - ``Formstück: Indikator Fließzustand``
     - ``[]``
   * - ``FITT_SUBTYPE``
     - ``Formstück: Details``
     - ``[3Sname]``
   * - ``FITT_VBTYPE1``
     - ``Formstück: Typ Verbindungselement 1``
     - ``[3Sname]``
   * - ``FITT_VBTYPE2``
     - ``Formstück: Typ Verbindungselement 2``
     - ``[3Sname]``
   * - ``FITT_VBTYPE3``
     - ``Formstück: Typ Verbindungselement 3``
     - ``[3Sname]``
   * - ``FITT_ZETA1``
     - ``Formstück: Einzelverlustbeiw. am VBEL 1``
     - ``[]``
   * - ``FITT_ZETA2``
     - ``Formstück: Einzelverlustbeiw. am VBEL 2``
     - ``[]``
   * - ``FITT_ZETA3``
     - ``Formstück: Einzelverlustbeiw. am VBEL 3``
     - ``[]``
   * - ``FSTF_NAME``
     - ``Name der Stoffwertegruppe``
     - ``[3Sname]``
   * - ``GMIX_NAME``
     - ``Name des Gasgemisches``
     - ``[3Sname]``
   * - ``H``
     - ``Druckhöhe``
     - ``[mNN]``
   * - ``HI``
     - ``Heizwert``
     - ``[kWh/Nm3]``
   * - ``HMAX_INST``
     - ``Druckhöhenmaximum instationär``
     - ``[mNN]``
   * - ``HMIN_INST``
     - ``Druckhöhenminimum instationär``
     - ``[mNN]``
   * - ``HS``
     - ``Brennwert``
     - ``[kWh/Nm3]``
   * - ``IAKTIV``
     - ``Netztrennstatus``
     - ``[]``
   * - ``INDUV``
     - ``Indikator Unterversorgung``
     - ``[]``
   * - ``K``
     - ``Kompressibilitätszahl K``
     - ``[]``
   * - ``KP``
     - ``Kompressibilitätszahl Kp``
     - ``[]``
   * - ``KT``
     - ``Kompressibilitätszahl KT``
     - ``[]``
   * - ``LEITFAEH``
     - ``Leitfähigkeit``
     - ``[muS/cm]``
   * - ``LFAKTAKT``
     - ``Aktueller Lastfaktor``
     - ``[]``
   * - ``LFKT``
     - ``Name Lastgangtabelle``
     - ``[3Sname]``
   * - ``M``
     - ``Externer Massenstrom``
     - ``[kg/s]``
   * - ``MAINELEMENT``
     - 
     - 
   * - ``MN``
     - ``Methanzahl``
     - ``[]``
   * - ``P``
     - ``Druck``
     - ``[bar,a]``
   * - ``PDAMPF``
     - ``Dampfdruck``
     - ``[bar,a]``
   * - ``PH``
     - ``Druck``
     - ``[bar]``
   * - ``PHMINMAXDIF``
     - ``Druckabweichung zum Mindestdruck``
     - ``[bar]``
   * - ``PHWERT``
     - ``pH-Wert``
     - ``[]``
   * - ``PH_EIN``
     - ``Druck in Eingabeeinheiten``
     - ``[bar]``
   * - ``PH_MIN``
     - ``Mindestknotendruck bei Entnahme``
     - ``[bar]``
   * - ``PMAX_INST``
     - ``Druckmaximum instationär``
     - ``[bar,a]``
   * - ``PMIN_INST``
     - ``Druckminimum instationär``
     - ``[bar,a]``
   * - ``PVAR``
     - ``Name Zeittabelle Druck-/Druckhöhe``
     - ``[3Sname]``
   * - ``Q2``
     - ``Externer Volumenstrom (altern. Einheit)``
     - ``[IDQM,5]``
   * - ``QM``
     - ``Externer Durchfluss``
     - ``[m3/h]``
   * - ``QMABS``
     - ``Externer Durchfluss Absolutbetrag``
     - ``[m3/h]``
   * - ``QVAR``
     - ``Name Zeittabelle Durchfluss``
     - ``[3Sname]``
   * - ``RHO``
     - ``Dichte``
     - ``[kg/m3]``
   * - ``RHON``
     - ``Normdichte``
     - ``[kg/m3]``
   * - ``RHONQUAL``
     - ``Normdichte (Qualitätsparameter)``
     - ``[kg/m3]``
   * - ``SULFAT``
     - ``Sulfat``
     - ``[mg/l]``
   * - ``T``
     - ``Temperatur``
     - ``[°C]``
   * - ``TE``
     - ``Einspeisetemperatur bei Zufluss``
     - ``[°C]``
   * - ``TEMP``
     - ``Temperatur (Wasserqualität)``
     - ``[°C]``
   * - ``TMAX_INST``
     - ``Temperaturmaximum instationär``
     - ``[°C]``
   * - ``TMIN_INST``
     - ``Temperaturminimum instationär``
     - ``[°C]``
   * - ``TTR``
     - ``Fluidalter``
     - ``[h]``
   * - ``VOLD``
     - ``Dampfvolumen``
     - ``[m3]``
   * - ``WALTER``
     - ``Wasseralter``
     - ``[h]``
   * - ``ZHKNR``
     - ``Nummer Zusammenhangskomponente``
     - ``[]``

KOMK
^^^^
Object Type: ``CompressorTable``


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

KOMK_ROWS
^^^^^^^^^
Object Type: ``CompressorTable_Row``


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

KOMP
^^^^
Object Type: ``Compressor``


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
     - Description
     - Standard Physical Unit
   * - ``DP``
     - ``Druckerhöhung``
     - ``[bar]``
   * - ``DT``
     - ``Temperaturerhöhung``
     - ``[K]``
   * - ``EINAUS``
     - ``Verdichter ein/aus``
     - ``[]``
   * - ``ETAP``
     - ``Prozess-Wirkungsgrad``
     - ``[]``
   * - ``IAKTIV``
     - ``Netztrennstatus``
     - ``[]``
   * - ``IND``
     - ``Betriebsstatus``
     - ``[]``
   * - ``INDANT``
     - ``Antriebsstatus``
     - ``[]``
   * - ``M``
     - ``Massenstrom``
     - ``[kg/s]``
   * - ``MAINELEMENT``
     - 
     - 
   * - ``N``
     - ``Drehzahl``
     - ``[1/min]``
   * - ``P``
     - ``Leistung``
     - ``[kW]``
   * - ``PE``
     - ``Energieverbrauch``
     - ``[kW]``
   * - ``PI``
     - ``Ansaugdruck``
     - ``[bar]``
   * - ``PK``
     - ``Ausgangsdruck``
     - ``[bar]``
   * - ``PMAX``
     - ``Maximal verfügbare Antriebsleistung``
     - ``[kW]``
   * - ``PRATIO``
     - ``Verdichtungsverhältnis``
     - ``[]``
   * - ``QN``
     - ``Durchfluss``
     - ``[(N)m3/h]``
   * - ``QNBG``
     - ``Brenngasverbrauch``
     - ``[(N)m3/h]``
   * - ``QNGES``
     - ``Durchfluss Kompressor Gesamtsystem``
     - ``[(N)m3/h]``
   * - ``TI``
     - ``Ansaugtemperatur``
     - ``[°C]``
   * - ``TK``
     - ``Ausgangstemperatur``
     - ``[°C]``
   * - ``YP``
     - ``Prozess-Referenzarbeit``
     - ``[kJ/kg]``

LAYR
^^^^
Object Type: ``LAYR_Layer``


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

LFKT
^^^^
Object Type: ``LoadFactorTable``


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
     - Description
     - Standard Physical Unit
   * - ``FWVB_DPHMIN``
     - ``Min. Differenzdruck Verbrauchergruppe``
     - ``[bar]``
   * - ``FWVB_TVLMIN``
     - ``Min. VL-Temperatur Verbrauchergruppe``
     - ``[°C]``
   * - ``LF``
     - ``Tabellensollwert Lastfaktor``
     - ``[]``
   * - ``MAINELEMENT``
     - 
     - 
   * - ``MFVHYUV``
     - ``Fehlmenge aus hydr. UV in VERB-Gruppe``
     - ``[t/h]``
   * - ``MFVTHUV``
     - ``Fehlmenge aus therm. UV in VERB-Gruppe``
     - ``[t/h]``
   * - ``NFVHYUV``
     - ``Anzahl FWVB mit hydr. UV in VERB-Gruppe``
     - ``[]``
   * - ``NFVTHUV``
     - ``Anzahl FWVB mit ther. UV in VERB-Gruppe``
     - ``[]``
   * - ``TVMINMAX``
     - ``Max der erf. min. VL-Temp in VERB-Gruppe``
     - ``[°C]``

LFKT_ROWT
^^^^^^^^^
Object Type: ``LoadFactorTable_Row``


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

LTGR
^^^^
Object Type: ``PipeGroup``


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

MREG
^^^^
Object Type: ``FlowControlUnit``


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
     - Description
     - Standard Physical Unit
   * - ``DH``
     - ``Differenzdruckhöhe``
     - ``[m]``
   * - ``DP``
     - ``Differenzdruck``
     - ``[bar]``
   * - ``DPH``
     - ``Reibungsdruckverlust/-druckverlusthöhe``
     - ``[bar]``
   * - ``DSI``
     - ``dynamische Stützkraft Knoten I``
     - ``[N|kN|MN]``
   * - ``DSK``
     - ``dynamische Stützkraft Knoten K``
     - ``[N|kN|MN]``
   * - ``FS``
     - ``dynamische axiale Last``
     - ``[N|kN|MN]``
   * - ``HR``
     - ``Reibungsdruckverlusthöhe``
     - ``[m]``
   * - ``IAKTIV``
     - ``Netztrennstatus``
     - ``[]``
   * - ``IND``
     - ``Betriebsart``
     - ``[]``
   * - ``KV``
     - ``KV-Wert``
     - ``[m3/h]``
   * - ``M``
     - ``Massenstrom``
     - ``[kg/s]``
   * - ``MAINELEMENT``
     - 
     - 
   * - ``PHI``
     - ``Reglerstellung``
     - ``[%]``
   * - ``PHISOLL``
     - ``Sollwert Reglerstellung``
     - ``[%]``
   * - ``PR``
     - ``Reibungsdruckverlust``
     - ``[bar]``
   * - ``Q``
     - ``Volumenstrom``
     - ``[m3/s]``
   * - ``QM``
     - ``Durchfluss``
     - ``[m3/h]``
   * - ``QMSOLL``
     - ``Konstanter Sollwert Menge``
     - ``[m3/h]``
   * - ``RHO``
     - ``Dichte``
     - ``[kg/m3]``
   * - ``SWVTPHI``
     - ``Name Sollwerttabelle Stellung``
     - ``[3Sname]``
   * - ``SWVTQM``
     - ``Name Sollwerttabelle Durchfluss``
     - ``[3Sname]``
   * - ``V``
     - ``Strömungsgeschwindigkeit``
     - ``[m/s]``
   * - ``ZETA``
     - ``Verlustbeiwert``
     - ``[]``

NRCV
^^^^
Object Type: ``NumericalDisplay``


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

NSCH
^^^^
Object Type: ``NetValve``


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
     - Description
     - Standard Physical Unit
   * - ``MAINELEMENT``
     - 
     - 
   * - ``STELLUNG``
     - ``Stellung Auf/Zu``
     - ``[]``

OBEH
^^^^
Object Type: ``OpenContainer``


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
     - Description
     - Standard Physical Unit
   * - ``DWST_DT``
     - ``Wasserstandsänderung``
     - ``[m/h]``
   * - ``IAKTIV``
     - ``Netztrennstatus``
     - ``[]``
   * - ``M``
     - ``Massenstrom``
     - ``[kg/s]``
   * - ``MAINELEMENT``
     - 
     - 
   * - ``MEXT``
     - ``Massenstrom aus Behälterbefüllung``
     - ``[kg/s]``
   * - ``QM``
     - ``Durchfluss``
     - ``[m3/h]``
   * - ``QMEXT``
     - ``Durchfluss aus Behälterbefüllung``
     - ``[m3/h]``
   * - ``RHO``
     - ``Dichte``
     - ``[kg/m3]``
   * - ``T``
     - ``Fluidtemperatur``
     - ``[°C]``
   * - ``T0``
     - ``Anfangsfluidtemperatur``
     - ``[°C]``
   * - ``V``
     - ``Strömungsgeschwindigkeit Anschluss``
     - ``[m/s]``
   * - ``VOL``
     - ``Wasservolumen``
     - ``[m3]``
   * - ``WALTER``
     - ``Wasseralter``
     - ``[h]``
   * - ``WALTER0``
     - ``Anfangswasseralter``
     - ``[h]``
   * - ``WST``
     - ``Wasserstand``
     - ``[m]``
   * - ``WST0``
     - ``Anfangswasserstand``
     - ``[m]``

OVAL
^^^^
Object Type: ``Oval``


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

PARI
^^^^
Object Type: ``CalcPari``


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

PARZ
^^^^
Object Type: ``PARZ_TransientCalculationParameters``


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

PGRP
^^^^
Object Type: ``PumpGroup``


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
     - Description
     - Standard Physical Unit
   * - ``BK``
     - ``Betriebskosten``
     - ``[EUR/h]``
   * - ``DH``
     - ``Förderhöhe``
     - ``[m]``
   * - ``DP``
     - ``Druckerhöhung``
     - ``[bar]``
   * - ``DPH``
     - ``Druckerhöhung/Förderhöhe``
     - ``[bar]``
   * - ``ETA``
     - ``Wirkungsgrad``
     - ``[]``
   * - ``IAKTIV``
     - ``Aktivität``
     - ``[]``
   * - ``INDPG``
     - ``Betriebsart``
     - ``[]``
   * - ``INDSTD``
     - ``Indikator Regelungsart``
     - ``[]``
   * - ``IZSTPG``
     - ``Zustand Restriktion``
     - ``[]``
   * - ``M``
     - ``Gesamtmassenstrom``
     - ``[kg/s]``
   * - ``MAINELEMENT``
     - 
     - 
   * - ``NPUMPIST``
     - ``Anzahl eingesetzter Pumpen``
     - ``[]``
   * - ``NPUMPSOLL``
     - ``Anzahl aktiver Pumpen``
     - ``[]``
   * - ``PE``
     - ``Gesamtklemmleistung``
     - ``[kW]``
   * - ``QM``
     - ``Gesamtdurchfluss``
     - ``[m3/h]``
   * - ``RART``
     - ``Name Regelungsart``
     - ``[3Sname]``
   * - ``RHO``
     - ``Dichte``
     - ``[kg/m3]``
   * - ``W``
     - ``Sollwert zur Regelungsart``
     - ``[unitX]``
   * - ``X``
     - ``Istwert zur Regelungsart``
     - ``[unitX]``

PGRP_PUMP
^^^^^^^^^
Object Type: ``PumpOfPumpGroup``


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
     - Description
     - Standard Physical Unit
   * - ``IAKTIV``
     - ``Aktivität``
     - ``[]``
   * - ``MAINELEMENT``
     - 
     - 

PHI1
^^^^
Object Type: ``ValveLiftTable``


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
     - Description
     - Standard Physical Unit
   * - ``MAINELEMENT``
     - 
     - 
   * - ``PHI``
     - ``Tabellensollwert Stellung``
     - ``[%]``

PHI1_ROWT
^^^^^^^^^
Object Type: ``ValveLiftTable_Row``


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

PHI2
^^^^
Object Type: ``VentOpenCloseTable``


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

PHI2_ROWS
^^^^^^^^^
Object Type: ``VentOpenCloseTable_Row``


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

PHIV
^^^^
Object Type: ``NonReturnValvesTable``


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

PHIV_ROWS
^^^^^^^^^
Object Type: ``NonReturnValvesTable_Row``


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

PHTR
^^^^
Object Type: ``PhaseSeparation``


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
     - Description
     - Standard Physical Unit
   * - ``DH``
     - ``Differenzdruckhöhe``
     - ``[m]``
   * - ``DP``
     - ``Differenzdruck``
     - ``[bar]``
   * - ``IAKTIV``
     - ``Netztrennstatus``
     - ``[]``
   * - ``MAINELEMENT``
     - 
     - 
   * - ``MI``
     - ``Massenstrom Knoten I``
     - ``[kg/s]``
   * - ``MK``
     - ``Massenstrom Knoten K``
     - ``[kg/s]``
   * - ``Q``
     - ``Volumenstrom``
     - ``[m3/s]``
   * - ``QM``
     - ``Durchfluss Knoten I``
     - ``[m3/h]``
   * - ``RHOI``
     - ``Dichte Knoten I``
     - ``[kg/m3]``
   * - ``RHOK``
     - ``Dichte Knoten K``
     - ``[kg/m3]``
   * - ``V``
     - ``Strömungsgeschwindigkeit``
     - ``[m/s]``

PLYG
^^^^
Object Type: ``Polygon``


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

POLY
^^^^
Object Type: ``Polyline``


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

PREG
^^^^
Object Type: ``PressureRegulator``


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
     - Description
     - Standard Physical Unit
   * - ``DH``
     - ``Differenzdruckhöhe``
     - ``[m]``
   * - ``DP``
     - ``Differenzdruck``
     - ``[bar]``
   * - ``DPH``
     - ``Reibungsdruckverlust/-druckverlusthöhe``
     - ``[bar]``
   * - ``DSI``
     - ``dynamische Stützkraft Knoten I``
     - ``[N|kN|MN]``
   * - ``DSK``
     - ``dynamische Stützkraft Knoten K``
     - ``[N|kN|MN]``
   * - ``FS``
     - ``dynamische axiale Last``
     - ``[N|kN|MN]``
   * - ``HR``
     - ``Reibungsdruckverlusthöhe``
     - ``[m]``
   * - ``IAKTIV``
     - ``Netztrennstatus``
     - ``[]``
   * - ``KV``
     - ``KV-Wert``
     - ``[m3/h]``
   * - ``M``
     - ``Massenstrom``
     - ``[kg/s]``
   * - ``MAINELEMENT``
     - 
     - 
   * - ``PH``
     - ``Istwert Druck/Druckhöhe``
     - ``[bar]``
   * - ``PHI``
     - ``Reglerstellung``
     - ``[%]``
   * - ``PHSOLL``
     - ``Sollwert Druck/Druckhöhe``
     - ``[bar]``
   * - ``PR``
     - ``Reibungsdruckverlust``
     - ``[bar]``
   * - ``PSOLL``
     - ``Sollwert Druck``
     - ``[bar,a]``
   * - ``QM``
     - ``Durchfluss``
     - ``[m3/h]``
   * - ``RHO``
     - ``Dichte``
     - ``[kg/m3]``
   * - ``SWVT``
     - ``Name Sollwerttabelle Druck``
     - ``[3Sname]``
   * - ``V``
     - ``Strömungsgeschwindigkeit``
     - ``[m/s]``
   * - ``ZETA``
     - ``Verlustbeiwert``
     - ``[]``

PUMD
^^^^
Object Type: ``PumpSpeedTable``


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
     - Description
     - Standard Physical Unit
   * - ``MAINELEMENT``
     - 
     - 
   * - ``N``
     - ``Tabellensollwert Drehzahl``
     - ``[1/min]``

PUMD_ROWT
^^^^^^^^^
Object Type: ``PumpSpeedTable_Row``


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

PUMK
^^^^
Object Type: ``PumpCharTable``


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

PUMK_ROWS
^^^^^^^^^
Object Type: ``PumpCharTable_Row``


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

PUMP
^^^^
Object Type: ``Pump``


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
     - Description
     - Standard Physical Unit
   * - ``BK``
     - ``Betriebskosten``
     - ``[EUR/h]``
   * - ``DH``
     - ``Förderhöhe``
     - ``[m]``
   * - ``DP``
     - ``Druckerhöhung``
     - ``[bar]``
   * - ``DPH``
     - ``Druckerhöhung/Förderhöhe``
     - ``[bar]``
   * - ``EINAUS``
     - ``Pumpe ein/aus``
     - ``[]``
   * - ``ETA``
     - ``Wirkungsgrad``
     - ``[]``
   * - ``ETAW``
     - ``Wellenwirkungsgrad``
     - ``[]``
   * - ``IAKTIV``
     - ``Netztrennstatus``
     - ``[]``
   * - ``IND``
     - ``Betriebsstatus``
     - ``[]``
   * - ``M``
     - ``Massenstrom``
     - ``[kg/s]``
   * - ``MAINELEMENT``
     - 
     - 
   * - ``MOM``
     - ``Drehmoment``
     - ``[Nm]``
   * - ``N``
     - ``Drehzahl``
     - ``[1/min]``
   * - ``NMINMAXDIF``
     - ``Drehzahlabweichung zum Arbeitsbereich``
     - ``[1/min]``
   * - ``NPSH``
     - ``NPSH aktuell``
     - ``[m]``
   * - ``NPSHDIF``
     - ``NPSH Abstand``
     - ``[m]``
   * - ``NPSHMIN``
     - ``NPSH erforderlich``
     - ``[m]``
   * - ``NSOLLTURB``
     - ``Sollwert Turbinendrehzahl``
     - ``[1/min]``
   * - ``PA``
     - ``Pumpenantriebsleistung``
     - ``[kW]``
   * - ``PE``
     - ``Klemmleistung``
     - ``[kW]``
   * - ``PE_RUECK``
     - ``Leistung aus Energie-Rückgewinnung``
     - ``[kW]``
   * - ``PHSOLL``
     - ``Sollwert Druck/Druckhöhe``
     - ``[bar]``
   * - ``PP``
     - ``Pumpenleistung, Wellenleistung``
     - ``[kW]``
   * - ``PUMD``
     - ``Name Drehzahltabelle``
     - ``[3Sname]``
   * - ``QM``
     - ``Durchfluss``
     - ``[m3/h]``
   * - ``QMSOLL``
     - ``Solldurchfluss Pumpe``
     - ``[m3/h]``
   * - ``QMSOLLTURB``
     - ``Solldurchfluss Turbine``
     - ``[m3/h]``
   * - ``QN0``
     - ``Durchfluss bei Nenndrehzahl``
     - ``[m3/h]``
   * - ``RCPU_IND``
     - ``Betriebsstatus RCPU-Zugriff``
     - ``[]``
   * - ``RCPU_W``
     - ``Sollwert aus Regelung``
     - ``[unitX]``
   * - ``RCPU_X``
     - ``Istwert aus Regelung``
     - ``[unitX]``
   * - ``RCPU_XD``
     - ``Regeldifferenz aus Regelung``
     - ``[unitX]``
   * - ``RHO``
     - ``Dichte``
     - ``[kg/m3]``
   * - ``STOERUNG``
     - ``Pumpenstörung``
     - ``[]``
   * - ``SWVT``
     - ``Name Sollwerttabelle``
     - ``[3Sname]``

PVAR
^^^^
Object Type: ``VarPressureTable``


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
     - Description
     - Standard Physical Unit
   * - ``MAINELEMENT``
     - 
     - 
   * - ``PH``
     - ``Tabellensollwert Druck``
     - ``[bar]``

PVAR_ROWT
^^^^^^^^^
Object Type: ``VarPressureTable_Row``


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

PZON
^^^^
Object Type: ``PressureZone``


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

QVAR
^^^^
Object Type: ``VarFlowTable``


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
     - Description
     - Standard Physical Unit
   * - ``FWVB_DPHMIN``
     - ``Min. Differenzdruck Verbrauchergruppe``
     - ``[bar]``
   * - ``FWVB_TVLMIN``
     - ``Min. VL-Temperatur Verbrauchergruppe``
     - ``[°C]``
   * - ``MAINELEMENT``
     - 
     - 
   * - ``MFVHYUV``
     - ``Fehlmenge aus hydr. UV Verbrauchergruppe``
     - ``[t/h]``
   * - ``MFVTHUV``
     - ``Fehlmenge aus therm. UV. VERB-Gruppe``
     - ``[t/h]``
   * - ``NFVHYUV``
     - ``Anzahl FWVB mit hydr. UV. VERB-Gruppe``
     - ``[]``
   * - ``NFVTHUV``
     - ``Anzahl FWVB mit therm. UV. VERB-Gruppe``
     - ``[]``
   * - ``QM``
     - ``Tabellensollwert Durchfluss``
     - ``[m3/h]``
   * - ``TVMINMAX``
     - ``Max der erf. min. VL-Temp VERB-Gruppe``
     - ``[°C]``

QVAR_ROWT
^^^^^^^^^
Object Type: ``VarFlowTable_Row``


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

RADD
^^^^
Object Type: ``SummingPoint``


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
     - Description
     - Standard Physical Unit
   * - ``MAINELEMENT``
     - 
     - 
   * - ``XA``
     - ``Signalwert am Ausgang``
     - ``[signal]``
   * - ``XE1``
     - ``Signalwert am Eingang 1``
     - ``[signal]``
   * - ``XE2``
     - ``Signalwert am Eingang 2``
     - ``[signal]``

RART
^^^^
Object Type: ``ControlMode``


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
     - Description
     - Standard Physical Unit
   * - ``MAINELEMENT``
     - 
     - 
   * - ``RCPL``
     - ``Name Regelpunktliste``
     - ``[3Sname]``
   * - ``SWVT``
     - ``Name Sollwerttabelle``
     - ``[3Sname]``
   * - ``W``
     - ``Sollwert zur Regelungsart``
     - ``[unitX]``

RCPL
^^^^
Object Type: ``ControlPointTable``


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
     - Description
     - Standard Physical Unit
   * - ``KNOT``
     - ``Name Schlechtpunkt``
     - ``[3Sname]``
   * - ``MAINELEMENT``
     - 
     - 
   * - ``W``
     - ``Sollwert Druck/Druckhöhe Schlechtpunkt``
     - ``[bar]``
   * - ``X``
     - ``Istwert Druck/Druckhöhe Schlechtpunkt``
     - ``[bar]``
   * - ``XD``
     - ``Regeldiff. Druck/Druckhöhe Schlechtpunkt``
     - ``[bar]``

RCPL_ROWT
^^^^^^^^^
Object Type: ``ControlPointTable_Row``


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
     - Description
     - Standard Physical Unit
   * - ``MAINELEMENT``
     - 
     - 
   * - ``W``
     - 
     - 
   * - ``X``
     - 
     - 
   * - ``XD``
     - 
     - 

RDIV
^^^^
Object Type: ``Divider``


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
     - Description
     - Standard Physical Unit
   * - ``MAINELEMENT``
     - 
     - 
   * - ``XA``
     - ``Signalwert am Ausgang``
     - ``[signal]``
   * - ``XE1``
     - ``Signalwert am Eingang 1``
     - ``[signal]``
   * - ``XE2``
     - ``Signalwert am Eingang 2``
     - ``[signal]``

RECT
^^^^
Object Type: ``Rectangle``


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

REGP
^^^^
Object Type: ``REGP_ControlParameters``


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

REGV
^^^^
Object Type: ``ControlValve``


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
     - Description
     - Standard Physical Unit
   * - ``DH``
     - ``Differenzdruckhöhe``
     - ``[m]``
   * - ``DP``
     - ``Differenzdruck``
     - ``[bar]``
   * - ``DPH``
     - ``Reibungsdruckverlust/-druckverlusthöhe``
     - ``[bar]``
   * - ``DSI``
     - ``dynamische Stützkraft Knoten I``
     - ``[N|kN|MN]``
   * - ``DSK``
     - ``dynamische Stützkraft Knoten K``
     - ``[N|kN|MN]``
   * - ``FS``
     - ``dynamische axiale Last``
     - ``[N|kN|MN]``
   * - ``HR``
     - ``Reibungsdruckverlusthöhe``
     - ``[m]``
   * - ``IAKTIV``
     - ``Netztrennstatus``
     - ``[]``
   * - ``INDSTD``
     - ``Indikator aus Regelungsart``
     - ``[]``
   * - ``KV``
     - ``KV-Wert``
     - ``[m3/h]``
   * - ``M``
     - ``Massenstrom``
     - ``[kg/s]``
   * - ``MAINELEMENT``
     - 
     - 
   * - ``PHI``
     - ``Reglerstellung``
     - ``[%]``
   * - ``PR``
     - ``Reibungsdruckverlust``
     - ``[bar]``
   * - ``Q2``
     - ``Volumenstrom (altern. Einheit)``
     - ``[IDQM,5]``
   * - ``QM``
     - ``Durchfluss``
     - ``[m3/h]``
   * - ``RART``
     - ``Name Regelungsart``
     - ``[3Sname]``
   * - ``RHO``
     - ``Dichte``
     - ``[kg/m3]``
   * - ``V``
     - ``Strömungsgeschwindigkeit``
     - ``[m/s]``
   * - ``W``
     - ``Sollwert zur Regelungsart``
     - ``[unitX]``
   * - ``X``
     - ``Istwert zur Regelungsart``
     - ``[unitX]``
   * - ``ZETA``
     - ``Verlustbeiwert``
     - ``[]``

RFKT
^^^^
Object Type: ``FunctionGenerator``


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
     - Description
     - Standard Physical Unit
   * - ``LFKT``
     - ``Name der verwendeten Tabelle``
     - ``[3Sname]``
   * - ``MAINELEMENT``
     - 
     - 
   * - ``XA``
     - ``Signalwert am Ausgang``
     - ``[signal]``
   * - ``XE``
     - ``Signalwert am Eingang``
     - ``[signal]``

RHYS
^^^^
Object Type: ``Histeresis``


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
     - Description
     - Standard Physical Unit
   * - ``MAINELEMENT``
     - 
     - 
   * - ``XA``
     - ``Signalwert am Ausgang``
     - ``[signal]``
   * - ``XE``
     - ``Signalwert am Eingang``
     - ``[signal]``
   * - ``XO``
     - ``Wert oberer Schaltpunkt``
     - ``[signal]``
   * - ``XU``
     - ``Wert unterer Schaltpunkt``
     - ``[signal]``

RINT
^^^^
Object Type: ``Integrator``


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
     - Description
     - Standard Physical Unit
   * - ``MAINELEMENT``
     - 
     - 
   * - ``XA``
     - ``Signalwert am Ausgang``
     - ``[signal]``
   * - ``XE``
     - ``Signalwert am Eingang``
     - ``[signal]``

RLSR
^^^^
Object Type: ``LogicalStorage``


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
     - Description
     - Standard Physical Unit
   * - ``MAINELEMENT``
     - 
     - 
   * - ``XA``
     - ``Signalwert am Ausgang``
     - ``[signal]``
   * - ``XE1``
     - ``Signalwert am Eingang 1``
     - ``[signal]``
   * - ``XE2``
     - ``Signalwert am Eingang 2``
     - ``[signal]``

RLVG
^^^^
Object Type: ``LogicalComparison``


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
     - Description
     - Standard Physical Unit
   * - ``MAINELEMENT``
     - 
     - 
   * - ``XA``
     - ``Signalwert am Ausgang``
     - ``[signal]``
   * - ``XE1``
     - ``Signalwert am Eingang 1``
     - ``[signal]``
   * - ``XE2``
     - ``Signalwert am Eingang 2``
     - ``[signal]``

RMES
^^^^
Object Type: ``Transmitter``


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
     - Description
     - Standard Physical Unit
   * - ``MAINELEMENT``
     - 
     - 
   * - ``XA``
     - ``Signalwert am Ausgang``
     - ``[signal]``
   * - ``XM``
     - ``Physikalischer Messwert``
     - ``[unitX]``
   * - ``XU``
     - ``Messwert nach Funktionsgeber``
     - ``[signal]``

RMES_DPTS
^^^^^^^^^
Object Type: ``RMES_DPTS_RmesInternalDataPoint``


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

RMMA
^^^^
Object Type: ``MinMaxSelection``


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
     - Description
     - Standard Physical Unit
   * - ``MAINELEMENT``
     - 
     - 
   * - ``XA``
     - ``Signalwert am Ausgang``
     - ``[signal]``
   * - ``XE1``
     - ``Signalwert am Eingang 1``
     - ``[signal]``
   * - ``XE2``
     - ``Signalwert am Eingang 2``
     - ``[signal]``

RMUL
^^^^
Object Type: ``Multiplier``


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
     - Description
     - Standard Physical Unit
   * - ``MAINELEMENT``
     - 
     - 
   * - ``MULT``
     - ``Multiplikator``
     - ``[]``
   * - ``XA``
     - ``Signalwert am Ausgang``
     - ``[signal]``
   * - ``XE1``
     - ``Signalwert am Eingang 1``
     - ``[signal]``
   * - ``XE2``
     - ``Signalwert am Eingang 2``
     - ``[signal]``

ROHR
^^^^
Object Type: ``Pipe``


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
     - Description
     - Standard Physical Unit
   * - ``A``
     - ``Schallgeschwindigkeit verwendet``
     - ``[m/s]``
   * - ``ACALC``
     - ``Schallgeschwindigkeit berechnet``
     - ``[m/s]``
   * - ``CPI``
     - ``Spezifische Wärmekapazität Rohranfang``
     - ``[kJ/kg/K]``
   * - ``CPK``
     - ``Spezifische Wärmekapazität Rohrende``
     - ``[kJ/kg/K]``
   * - ``DH``
     - ``Differenzdruckhöhe``
     - ``[m]``
   * - ``DP``
     - ``Differenzdruck``
     - ``[bar]``
   * - ``DRAGRED``
     - ``Widerstands-Reduzierung (DRA)``
     - ``[%]``
   * - ``DRAKONZ``
     - ``Fließverbesserer-Konzentration``
     - ``[ppm]``
   * - ``DSI``
     - ``dynamische Stützkraft Knoten I``
     - ``[N|kN|MN]``
   * - ``DSK``
     - ``dynamische Stützkraft Knoten K``
     - ``[N|kN|MN]``
   * - ``DTTR``
     - ``Fließdauer durch das Rohr``
     - ``[h]``
   * - ``DWVERL``
     - ``Spezifischer Wärmeverlust``
     - ``[W/m]``
   * - ``DWVERLABS``
     - ``Wärmeverlust``
     - ``[kW]``
   * - ``ETAAV``
     - ``Mittlere dynamische Viskosität``
     - ``[kg/(m*s)]``
   * - ``FS``
     - ``dynamische axiale Last``
     - ``[N|kN|MN]``
   * - ``HR``
     - ``Reibungsdruckverlusthöhe``
     - ``[m]``
   * - ``HVEC``
     - ``Druckhöhen Rohrgitter``
     - ``[mNN]``
   * - ``IAKTIV``
     - ``Netztrennstatus``
     - ``[]``
   * - ``IRTRENN``
     - ``Rohrtrennung``
     - ``[]``
   * - ``JV``
     - ``Spezifischer Reibungsdruckverlust``
     - ``[bar/km]``
   * - ``JV2``
     - ``Spezifischer Reibungsdruckverlust``
     - ``[Pa/m]``
   * - ``LAMBDA``
     - ``Reibungsbeiwert``
     - ``[]``
   * - ``LECKEINAUS``
     - ``Rohrleck aktivieren/deaktivieren``
     - ``[]``
   * - ``LECKMENGE``
     - ``Leckmenge``
     - ``[m3/h]``
   * - ``LECKORT``
     - ``Leckort``
     - ``[m]``
   * - ``LINEPACK``
     - ``Linepack``
     - ``[(N)m3]``
   * - ``LINEPACKGEOM``
     - ``Linepack Rohrinhalt``
     - ``[(N)m3]``
   * - ``LINEPACKRATE``
     - ``Linepack-Rate``
     - ``[(N)m3/h]``
   * - ``MAINELEMENT``
     - 
     - 
   * - ``MAV``
     - ``Mittlerer Massenstrom``
     - ``[kg/s]``
   * - ``MI``
     - ``Massenstrom Knoten I``
     - ``[kg/s]``
   * - ``MK``
     - ``Massenstrom Knoten K``
     - ``[kg/s]``
   * - ``MKOND``
     - 
     - 
   * - ``MMAX_INST``
     - ``Massenstrommaximum instationär``
     - ``[kg/s]``
   * - ``MMIN_INST``
     - ``Massenstromminimum instationär``
     - ``[kg/s]``
   * - ``MVEC``
     - ``Massenströme Rohrgitter``
     - ``[kg/s]``
   * - ``MVECMAX_INST``
     - ``Massenstrommaxima Rohrgitter instationär``
     - ``[kg/s]``
   * - ``MVECMIN_INST``
     - ``Massenstromminima Rohrgitter instationär``
     - ``[kg/s]``
   * - ``PAV``
     - ``Mittlerer Druck``
     - ``[bar,a]``
   * - ``PDAMPF``
     - ``Mittleres Dampfdruckniveau``
     - ``[bar,a]``
   * - ``PHR``
     - ``Reibungsdruckverlust/-druckverlusthöhe``
     - ``[bar]``
   * - ``PHVEC``
     - ``Drücke Rohrgitter``
     - ``[bar]``
   * - ``PMAX``
     - ``Größter Druck``
     - ``[bar,a]``
   * - ``PMIN``
     - ``Kleinster Druck``
     - ``[bar,a]``
   * - ``PR``
     - ``Reibungsdruckverlust``
     - ``[bar]``
   * - ``PVEC``
     - ``Drücke Rohrgitter``
     - ``[bar,a]``
   * - ``PVECMAX_INST``
     - ``Druckmaxima Rohrgitter instationär``
     - ``[bar,a]``
   * - ``PVECMIN_INST``
     - ``Druckminima Rohrgitter instationär``
     - ``[bar,a]``
   * - ``QI2``
     - ``Volumenstrom Knoten I (altern. Einheit)``
     - ``[IDQM,5]``
   * - ``QK2``
     - ``Volumenstrom Knoten K (altern. Einheit)``
     - ``[IDQM,5]``
   * - ``QMAV``
     - ``Mittlerer Volumenstrom``
     - ``[m3/h]``
   * - ``QMI``
     - ``Durchfluss Knoten I``
     - ``[m3/h]``
   * - ``QMK``
     - ``Durchfluss Knoten K``
     - ``[m3/h]``
   * - ``QMMAX_INST``
     - ``Durchflussmaximum instationär``
     - ``[m3/h]``
   * - ``QMMIN_INST``
     - ``Durchflussminimum instationär``
     - ``[m3/h]``
   * - ``QMVEC``
     - ``Durchfluss Rohrgitter``
     - ``[m3/h]``
   * - ``QSVB``
     - ``Strangabnahme``
     - ``[m3/h/m]``
   * - ``RHOAV``
     - ``Mittlere Dichte``
     - ``[kg/m3]``
   * - ``RHOI``
     - ``Dichte Rohranfang``
     - ``[kg/m3]``
   * - ``RHOK``
     - ``Dichte Rohrende``
     - ``[kg/m3]``
   * - ``RHOVEC``
     - ``Dichten Rohrgitter``
     - ``[kg/m3]``
   * - ``SVEC``
     - ``Weglängen Rohrgitter``
     - ``[m]``
   * - ``TAV``
     - ``Mittlere Temperatur``
     - ``[°C]``
   * - ``TI``
     - ``Temperatur Rohranfang``
     - ``[°C]``
   * - ``TK``
     - ``Temperatur Rohrende``
     - ``[°C]``
   * - ``TTRVEC``
     - ``Fluidalter Rohrgitter``
     - ``[h]``
   * - ``TVEC``
     - ``Temperaturen Rohrgitter``
     - ``[°C]``
   * - ``TVECMAX_INST``
     - ``Temperaturmaxima Rohrgitter instationär``
     - ``[°C]``
   * - ``TVECMIN_INST``
     - ``Temperaturminima Rohrgitter instationär``
     - ``[°C]``
   * - ``VAV``
     - ``Mittlere Strömungsgeschwindigkeit``
     - ``[m/s]``
   * - ``VI``
     - ``Strömungsgeschwindigkeit Knoten I``
     - ``[m/s]``
   * - ``VK``
     - ``Strömungsgeschwindigkeit Knoten K``
     - ``[m/s]``
   * - ``VMAX_INST``
     - ``Geschwindigkeitsmaximum instationär``
     - ``[m/s]``
   * - ``VMIN_INST``
     - ``Geschwindigkeitsminimum instationär``
     - ``[m/s]``
   * - ``VOLDA``
     - ``Dampfvolumen``
     - ``[m3]``
   * - ``WALTERI``
     - ``Wasseralter am Rohranfang``
     - ``[h]``
   * - ``WALTERK``
     - ``Wasseralter am Rohrende``
     - ``[h]``
   * - ``WVL``
     - ``Wärmestrom Vorlauf``
     - ``[kW]``
   * - ``ZAUS``
     - ``Einzelverlustbeiwert am Ausstromrand``
     - ``[]``
   * - ``ZEIN``
     - ``Einzelverlustbeiwert am Einstromrand``
     - ``[]``
   * - ``ZHKNR``
     - ``Teilgebietsnummer``
     - ``[]``
   * - ``ZVEC``
     - ``Geodätische Höhen Rohrgitter``
     - ``[m]``

ROHR_VRTX
^^^^^^^^^
Object Type: ``PipeVertex``


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
     - Description
     - Standard Physical Unit
   * - ``H``
     - ``Druckhöhe``
     - ``[mNN]``
   * - ``M``
     - ``Massenstrom``
     - ``[kg/s]``
   * - ``MAINELEMENT``
     - 
     - 
   * - ``MMAX_INST``
     - ``Massenstrommaximum instationär``
     - ``[kg/s]``
   * - ``MMIN_INST``
     - ``Massenstromminimum instationär``
     - ``[kg/s]``
   * - ``P``
     - ``Druck``
     - ``[bar,a]``
   * - ``PH``
     - ``Druck``
     - ``[bar]``
   * - ``PMAX_INST``
     - ``Druckmaximum instationär``
     - ``[bar,a]``
   * - ``PMIN_INST``
     - ``Druckminimum instationär``
     - ``[bar,a]``
   * - ``RHO``
     - ``Dichte``
     - ``[kg/m3]``
   * - ``T``
     - ``Temperatur``
     - ``[°C]``
   * - ``TMAX_INST``
     - ``Temperaturmaximum instationär``
     - ``[°C]``
   * - ``TMIN_INST``
     - ``Temperaturminimum instationär``
     - ``[°C]``

RPFL
^^^^
Object Type: ``DirectionalArrow``


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

RPID
^^^^
Object Type: ``PidController``


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
     - Description
     - Standard Physical Unit
   * - ``DYDT``
     - ``Verstellgeschwindigkeit gesamt``
     - ``[unitY/s]``
   * - ``DYDTD``
     - ``Verstellgeschwindigkeit differentiell``
     - ``[unitY/s]``
   * - ``DYDTI``
     - ``Verstellgeschwindigkeit integral``
     - ``[unitY/s]``
   * - ``DYDTP``
     - ``Verstellgeschwindigkeit proportional``
     - ``[unitY/s]``
   * - ``MAINELEMENT``
     - 
     - 
   * - ``XA``
     - ``Signalwert am Ausgang``
     - ``[signal]``
   * - ``XE1``
     - ``Signalwert am Eingang 1``
     - ``[signal]``
   * - ``XE2``
     - ``Signalwert am Eingang 2``
     - ``[signal]``

RPT1
^^^^
Object Type: ``Pt1Controller``


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
     - Description
     - Standard Physical Unit
   * - ``MAINELEMENT``
     - 
     - 
   * - ``XA``
     - ``Signalwert am Ausgang``
     - ``[signal]``
   * - ``XE``
     - ``Signalwert am Eingang``
     - ``[signal]``

RRCT
^^^^
Object Type: ``RoundRectangle``


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

RSLW
^^^^
Object Type: ``SetpointDevice``


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
     - Description
     - Standard Physical Unit
   * - ``LFKT``
     - ``Name Lastgangtabelle``
     - ``[3Sname]``
   * - ``MAINELEMENT``
     - 
     - 
   * - ``SLWKON``
     - ``Sollwert konstant``
     - ``[unitX]``
   * - ``SWVT``
     - ``Name Sollwerttabelle``
     - ``[3Sname]``
   * - ``W``
     - ``Vorgegebener Sollwert``
     - ``[unitX]``
   * - ``WAKT``
     - ``Aktueller Sollwert``
     - ``[unitX]``
   * - ``WE``
     - ``Normierter vorgegebener Sollwert``
     - ``[]``
   * - ``WEAKT``
     - ``Normierter aktueller Sollwert``
     - ``[]``
   * - ``WERCK``
     - ``Normierter rückgemeldeter Sollwert``
     - ``[]``
   * - ``WRCK``
     - ``Rückgemeldeter Sollwert``
     - ``[unitX]``
   * - ``XA``
     - ``Signalwert am Ausgang``
     - ``[signal]``

RSTE
^^^^
Object Type: ``ControlVariableConverterRSTE``


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
     - Description
     - Standard Physical Unit
   * - ``DYDT1``
     - ``Stellgrößenänderung Element 1``
     - ``[unitY/s]``
   * - ``DYDT2``
     - ``Stellgrößenänderung Element 2``
     - ``[unitY/s]``
   * - ``DYDT3``
     - ``Stellgrößenänderung Element 3``
     - ``[unitY/s]``
   * - ``DYDT4``
     - ``Stellgrößenänderung Element 4``
     - ``[unitY/s]``
   * - ``DYDT5``
     - ``Stellgrößenänderung Element 5``
     - ``[unitY/s]``
   * - ``MAINELEMENT``
     - 
     - 
   * - ``XE1``
     - ``Signalwert am Eingang 1``
     - ``[signal]``
   * - ``YS1``
     - ``Stellgröße Element 1``
     - ``[unitY]``
   * - ``YS2``
     - ``Stellgröße Element 2``
     - ``[unitY]``
   * - ``YS3``
     - ``Stellgröße Element 3``
     - ``[unitY]``
   * - ``YS4``
     - ``Stellgröße Element 4``
     - ``[unitY]``
   * - ``YS5``
     - ``Stellgröße Element 5``
     - ``[unitY]``

RSTN
^^^^
Object Type: ``ControlVariableConverter``


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
     - Description
     - Standard Physical Unit
   * - ``LFKT``
     - ``Name Lastgangtabelle``
     - ``[3Sname]``
   * - ``MAINELEMENT``
     - 
     - 
   * - ``PHI1``
     - ``Name Zeittabelle Stellung``
     - ``[3Sname]``
   * - ``PUMD``
     - ``Name Drehzahltabelle``
     - ``[3Sname]``
   * - ``PVAR``
     - ``Name Zeittabelle Druck-/Druckhöhe``
     - ``[3Sname]``
   * - ``QVAR``
     - ``Name Sollwerttabelle Durchfluss``
     - ``[3Sname]``
   * - ``SWVT``
     - ``Name Sollwerttabelle``
     - ``[3Sname]``
   * - ``TEVT``
     - ``Name Zeittabelle Speisetemperatur``
     - ``[3Sname]``
   * - ``TRGCOUNT``
     - ``Trigger Stellbefehl``
     - ``[]``
   * - ``WEVT``
     - ``Name Zeittabelle Wärmeleistung``
     - ``[3Sname]``
   * - ``XE1``
     - ``Signalwert am Eingang 1``
     - ``[signal]``
   * - ``XE2``
     - ``Signalwert am Eingang 2``
     - ``[signal]``

RTOT
^^^^
Object Type: ``DeadTimeElement``


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
     - Description
     - Standard Physical Unit
   * - ``MAINELEMENT``
     - 
     - 
   * - ``XA``
     - ``Signalwert am Ausgang``
     - ``[signal]``
   * - ``XE``
     - ``Signalwert am Eingang``
     - ``[signal]``

RUES
^^^^
Object Type: ``TransitionSymbol``


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

SIVE
^^^^
Object Type: ``SafetyValve``


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
     - Description
     - Standard Physical Unit
   * - ``DH``
     - ``Differenzdruckhöhe``
     - ``[m]``
   * - ``DP``
     - ``Differenzdruck``
     - ``[bar]``
   * - ``DPH``
     - ``Reibungsdruckverlust/-druckverlusthöhe``
     - ``[bar]``
   * - ``DSI``
     - ``dynamische Stützkraft Knoten I``
     - ``[N|kN|MN]``
   * - ``DSK``
     - ``dynamische Stützkraft Knoten K``
     - ``[N|kN|MN]``
   * - ``FS``
     - ``dynamische axiale Last``
     - ``[N|kN|MN]``
   * - ``HR``
     - ``Reibungsdruckverlusthöhe``
     - ``[m]``
   * - ``IAKTIV``
     - ``Netztrennstatus``
     - ``[]``
   * - ``M``
     - ``Massenstrom``
     - ``[kg/s]``
   * - ``MAINELEMENT``
     - 
     - 
   * - ``PHI``
     - ``Stellung``
     - ``[%]``
   * - ``PHSCH``
     - ``Schaltdruck``
     - ``[bar]``
   * - ``PR``
     - ``Reibungsdruckverlust``
     - ``[bar]``
   * - ``QM``
     - ``Durchfluss``
     - ``[m3/h]``
   * - ``RHO``
     - ``Dichte``
     - ``[kg/m3]``
   * - ``V``
     - ``Strömungsgeschwindigkeit``
     - ``[m/s]``
   * - ``ZETA``
     - ``Verlustbeiwert``
     - ``[]``

SOKO
^^^^
Object Type: ``SolarCollector``


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

SPLZ
^^^^
Object Type: ``SPLZ_TimeSeries``


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

SRAT
^^^^
Object Type: ``DamageRatesTable``


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

SRAT_ROWS
^^^^^^^^^
Object Type: ``DamageRatesTable_Row``


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

STOF
^^^^
Object Type: ``ThermophysPropTable``


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

STOF_ROWS
^^^^^^^^^
Object Type: ``ThermophysPropTable_Row``


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

STRASSE
^^^^^^^
Object Type: ``Street``


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

STRO
^^^^
Object Type: ``StandPipe``


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
     - Description
     - Standard Physical Unit
   * - ``IAKTIV``
     - ``Netztrennstatus``
     - ``[]``
   * - ``M``
     - ``Massenstrom``
     - ``[kg/s]``
   * - ``MAINELEMENT``
     - 
     - 
   * - ``MUEB``
     - ``Massenstrom Überfall``
     - ``[kg/s]``
   * - ``QM``
     - ``Durchfluss``
     - ``[m3/h]``
   * - ``QMUEB``
     - ``Durchfluss Überfall``
     - ``[m3/h]``
   * - ``RHO``
     - ``Dichte``
     - ``[kg/m3]``
   * - ``T``
     - ``Fluidtemperatur``
     - ``[°C]``
   * - ``V``
     - ``Strömungsgeschwindigkeit Anschluss``
     - ``[m/s]``
   * - ``VOL``
     - ``Wasservolumen``
     - ``[m3]``
   * - ``WALTER``
     - ``Wasseralter``
     - ``[h]``
   * - ``WST``
     - ``Wasserstand``
     - ``[m]``

SWVT
^^^^
Object Type: ``MeasuredVariableTable``


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
     - Description
     - Standard Physical Unit
   * - ``MAINELEMENT``
     - 
     - 
   * - ``W``
     - ``Tabellensollwert generisch``
     - ``[unitX]``

SWVT_ROWT
^^^^^^^^^
Object Type: ``MeasuredVariableTable_Row``


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

TEVT
^^^^
Object Type: ``TemperatureTable``


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
     - Description
     - Standard Physical Unit
   * - ``MAINELEMENT``
     - 
     - 
   * - ``T``
     - ``Tabellensollwert Temperatur``
     - ``[°C]``

TEVT_ROWT
^^^^^^^^^
Object Type: ``TemperatureTable_Row``


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

TFKT
^^^^
Object Type: ``FunctionTable``


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

TFKT_ROWS
^^^^^^^^^
Object Type: ``FunctionTable_Row``


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

TRFT
^^^^
Object Type: ``ReturnTemperaturTable``


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

TRFT_ROWS
^^^^^^^^^
Object Type: ``ReturnTemperaturTable_Row``


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

TRVA
^^^^
Object Type: ``TransportVariable``


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

USCH
^^^^
Object Type: ``USCH_UserDefinedProperties``


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

UTMP
^^^^
Object Type: ``EnvironmentTemp``


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

VARA
^^^^
Object Type: ``VARA_ColorScale``


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

VARA_ROWS
^^^^^^^^^
Object Type: ``VARA_ROWS_WidthOrScale``


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

VENT
^^^^
Object Type: ``Valve``


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
     - Description
     - Standard Physical Unit
   * - ``AUF``
     - ``Auffahren/Endlage Auf``
     - ``[]``
   * - ``AUFZU``
     - ``Ventil auf/zu``
     - ``[]``
   * - ``DH``
     - ``Differenzdruckhöhe``
     - ``[m]``
   * - ``DP``
     - ``Differenzdruck``
     - ``[bar]``
   * - ``DSI``
     - ``dynamische Stützkraft Knoten I``
     - ``[N|kN|MN]``
   * - ``DSK``
     - ``dynamische Stützkraft Knoten K``
     - ``[N|kN|MN]``
   * - ``FREIGABE``
     - ``Status Freigabe``
     - ``[]``
   * - ``FS``
     - ``dynamische axiale Last``
     - ``[N|kN|MN]``
   * - ``HR``
     - ``Reibungsdruckverlusthöhe``
     - ``[m]``
   * - ``IAKTIV``
     - ``Netztrennstatus``
     - ``[]``
   * - ``KV``
     - ``KV-Wert``
     - ``[m3/h]``
   * - ``LAEUFT``
     - ``Öffnet oder schließt``
     - ``[]``
   * - ``M``
     - ``Massenstrom``
     - ``[kg/s]``
   * - ``MAINELEMENT``
     - 
     - 
   * - ``OEFFNET``
     - ``Öffnet``
     - ``[]``
   * - ``PHI``
     - ``Stellung``
     - ``[%]``
   * - ``PHI1``
     - ``Name Zeittabelle Stellung``
     - ``[3Sname]``
   * - ``PHR``
     - ``Reibungsdruckverlust/-druckverlusthöhe``
     - ``[bar]``
   * - ``PR``
     - ``Reibungsdruckverlust``
     - ``[bar]``
   * - ``Q2``
     - ``Volumenstrom (altern. Einheit)``
     - ``[IDQM,5]``
   * - ``QM``
     - ``Durchfluss``
     - ``[m3/h]``
   * - ``RHO``
     - ``Dichte``
     - ``[kg/m3]``
   * - ``SCHLIESST``
     - ``Schließt``
     - ``[]``
   * - ``STOERUNG``
     - ``Ventilstörung``
     - ``[]``
   * - ``V``
     - ``Strömungsgeschwindigkeit``
     - ``[m/s]``
   * - ``ZETA``
     - ``Verlustbeiwert``
     - ``[]``
   * - ``ZU``
     - ``Zufahren/Endlage Zu``
     - ``[]``

VERB
^^^^
Object Type: ``Demand``


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

VKNO
^^^^
Object Type: ``BlockConnectionNode``


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

VRCT
^^^^
Object Type: ``VRCT_ViewRectangle``


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

WBLZ
^^^^
Object Type: ``WBLZ_ThermalBalance``


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
     - Description
     - Standard Physical Unit
   * - ``MAINELEMENT``
     - 
     - 
   * - ``WES``
     - ``Einspeiseleistung``
     - ``[KW|MW]``
   * - ``WRAND``
     - ``Wärmestrom Gebietsrand``
     - ``[KW|MW]``
   * - ``WSPEI``
     - ``Gespeicherte Leistung Rohrnetz``
     - ``[KW|MW]``
   * - ``WSPEI_SP``
     - ``Gespeicherte Leistung Wärmespeicher``
     - ``[KW|MW]``
   * - ``WVB``
     - ``Verbrauchsleistung Istwert``
     - ``[KW|MW]``
   * - ``WVB_0``
     - ``Verbrauchsleistung Auslegung``
     - ``[KW|MW]``
   * - ``WVB_W``
     - ``Verbrauchsleistung Sollwert``
     - ``[KW|MW]``
   * - ``WVB_XD``
     - ``Verbrauchsleistung Defizit``
     - ``[KW|MW]``
   * - ``WVERL``
     - ``Verlustleistung Rohrnetz``
     - ``[KW|MW]``
   * - ``WWU``
     - ``Wärmestrom Wärmeübertrager``
     - ``[KW|MW]``

WEVT
^^^^
Object Type: ``ThermalOutputTable``


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
     - Description
     - Standard Physical Unit
   * - ``MAINELEMENT``
     - 
     - 
   * - ``W``
     - ``Tabellensollwert Wärmeleistung``
     - ``[kW]``

WEVT_ROWT
^^^^^^^^^
Object Type: ``ThermalOutputTable_Row``


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

WIND
^^^^
Object Type: ``AirVessel``


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
     - Description
     - Standard Physical Unit
   * - ``HLUFT``
     - ``Druckhöhe im Gasvolumen``
     - ``[mNN]``
   * - ``IAKTIV``
     - ``Netztrennstatus``
     - ``[]``
   * - ``M``
     - ``Massenstrom``
     - ``[kg/s]``
   * - ``MAINELEMENT``
     - 
     - 
   * - ``PLUFT``
     - ``Druck im Gasvolumen``
     - ``[bar,a]``
   * - ``QM``
     - ``Durchfluss``
     - ``[m3/h]``
   * - ``RHO``
     - ``Dichte``
     - ``[kg/m3]``
   * - ``T``
     - ``Fluidtemperatur``
     - ``[°C]``
   * - ``V``
     - ``Strömungsgeschwindigkeit``
     - ``[m/s]``
   * - ``VOL``
     - ``Wasservolumen``
     - ``[m3]``
   * - ``VOLDA``
     - ``Dampfvolumen``
     - ``[m3]``
   * - ``VOLGAS``
     - ``Gasvolumen``
     - ``[m3]``
   * - ``WALTER``
     - ``Wasseralter``
     - ``[h]``
   * - ``WST``
     - ``Wasserstand``
     - ``[m]``

WTTR
^^^^
Object Type: ``WeatherDataTable``


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
     - Description
     - Standard Physical Unit
   * - ``GDIFF``
     - ``Diffusstrahlung``
     - ``[W/m²]``
   * - ``GGLOB``
     - ``Globalstrahlung``
     - ``[W/m²]``
   * - ``MAINELEMENT``
     - 
     - 
   * - ``TEMP``
     - ``Lufttemperatur``
     - ``[°C]``
   * - ``WIND``
     - ``Windgeschwindigkeit``
     - ``[m/s]``

WTTR_ROWT
^^^^^^^^^
Object Type: ``WeatherDataTable_Row``


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

ZEP1
^^^^
Object Type: ``RegulatorsTable``


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

ZEP1_ROWS
^^^^^^^^^
Object Type: ``RegulatorsTable_Row``


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

ZEP2
^^^^
Object Type: ``CharacteristicLossTable``


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

ZEP2_ROWS
^^^^^^^^^
Object Type: ``CharacteristicLossTable_Row``


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

