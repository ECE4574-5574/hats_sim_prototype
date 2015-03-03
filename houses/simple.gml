<graphml xmlns="http://graphml.graphdrawing.org/xmlns" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://graphml.graphdrawing.org/xmlns http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd">
  <key attr.name="name" attr.type="string" for="graph" id="d0" />
  <graph edgedefault="undirected">
    <data key="d0">test_house</data>
    <node id="kitchen" />
    <node id="living" />
    <node id="bathroom" />
    <node id="dining" />
    <node id="bedroom" />
    <node id="guest" />
    <node id="atrium" />
    <edge source="kitchen" target="living" />
    <edge source="living" target="atrium" />
    <edge source="kitchen" target="dining" />
    <edge source="atrium" target="dining" />
    <edge source="atrium" target="bedroom" />
    <edge source="atrium" target="guest" />
    <edge source="atrium" target="bathroom" />
  </graph>
</graphml>
