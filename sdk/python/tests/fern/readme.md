To run the test:
- Build and install the client library
- Run `conda env config vars set FEAST_AZ_AUTH_CLIENT_ID=8909bdfe-55e1-40fd-b295-58d3608297fd FEAST_AZ_AUTH_TENANT_ID=72f988bf-86f1-41af-91ab-2d7cd011db47` in Anaconda to set the information for AAD auth
- Run `python .\tests\fern\test.py`
- Sign in your AAD account using the device code