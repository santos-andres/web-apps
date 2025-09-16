#az login
az acr login -n dmwebapp

docker build -t quality_app:v1 .
docker tag quality_app:v1 dmwebapp.azurecr.io/quality_app:v1
docker push dmwebapp.azurecr.io/quality_app:v1



######### ______ For the first initialization ______ #########
<# az containerapp up `
  --name quality_web_app `
  --resource-group RG-SABCA4 `
  --location West Europe `
  --environment  my-container-apps `
  --image mcr.microsoft.com/azuredocs/containerapps-helloworld:latest `
  --target-port 80 `
  --ingress external `
  --query properties.configuration.ingress.fqdn
 #>
#need to create an app registration in AD before hand and get clientID, secret and tenant id
##az containerapp auth microsoft update --debug --verbose --name data-cleaning --resource-group datatopia-app-rg --client-id *** --client-secret *** --tenant-id ****

