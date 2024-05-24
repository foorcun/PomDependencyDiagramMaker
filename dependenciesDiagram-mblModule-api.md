```mermaid
 graph TD
esb-api --> mblModule-api
mblConfig --> mblModule-api
coreServicesService-api --> mblModule-api
dto --> mblModule-api
dataModel --> mblModule-api
internal --> mblModule-api
commons-lang3 --> mblModule-api
aspectjweaver --> mblModule-api
javax.servlet-api --> mblModule-api
cxf-rt-frontend-jaxrs --> mblModule-api
cxf-rt-rs-client --> mblModule-api
util --> mblModule-api
util --> mblModule-api
jsonassert --> mblModule-api
```


```sh
@startuml
esb_api -- mblModule_api
mblConfig -- mblModule_api
coreServicesService_api -- mblModule_api
dto -- mblModule_api
dataModel -- mblModule_api
internal -- mblModule_api
commons_lang3 -- mblModule_api
aspectjweaver -- mblModule_api
javax.servlet_api -- mblModule_api
cxf_rt_frontend_jaxrs -- mblModule_api
cxf_rt_rs_client -- mblModule_api
util -- mblModule_api
util -- mblModule_api
jsonassert -- mblModule_api
@enduml
```