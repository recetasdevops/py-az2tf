# azurerm_databricks_workspace
def azurerm_databricks_workspace(crf,cde,crg,headers,requests,sub,json,az2tfmess):
    tfp="azurerm_databricks_workspace"
    tcode="550-"
    azr=""
    if crf in tfp:
    # REST or cli
        print "REST Managed Disk"
        url="https://management.azure.com/subscriptions/" + sub + "/providers/Microsoft.Compute/disks"
        params = {'api-version': '2017-03-30'}
        r = requests.get(url, headers=headers, params=params)
        azr= r.json()["value"]
        if cde:
            print(json.dumps(azr, indent=4, separators=(',', ': ')))

        tfrmf=tcode+tfp+"-staterm.sh"
        tfimf=tcode+tfp+"-stateimp.sh"
        tfrm=open(tfrmf, 'a')
        tfim=open(tfimf, 'a')
        print tfp,
        count=len(azr)
        print count
        for i in range(0, count):

            name=azr[i]["name"]
            loc=azr[i]["location"]
            id=azr[i]["id"]
            rg=id.split("/")[4].replace(".","-")

            if crg is not None:
                if rg.lower() != crg.lower():
                    continue  # back to for
            
            rname=name.replace(".","-")
            prefix=tfp+"."+rg+'__'+rname
            #print prefix
            rfilename=prefix+".tf"
            fr=open(rfilename, 'w')
            fr.write(az2tfmess)
            fr.write('resource ' + tfp + ' ' + rg + '__' + rname + ' {\n')
            fr.write('\t name = "' + name + '"\n')
            fr.write('\t location = "'+ loc + '"\n')
            fr.write('\t resource_group_name = "'+ rg + '"\n')

    ###############
    # specific code start
    ###############


prefixa= 0 | awk -F 'azurerm_' '{'print 2}'' | cut -f1 -d'.'
tfp=fr.write('azurerm_" prefixa
echo ftp

if 1" != " :
    rgsource=1
else
    echo -n "Enter name of Resource Group [rgsource]["> "
    read response
    if [ -n "response" :
        rgsource=response
   
fi

echo TF_VAR_rgtarget
if 1" != " :
    rgsource=1
fi

at=az account get-access-token -o json
bt= at | jq .accessToken]
sub= at | jq .subscription]

ris2=fr.write('curl -s  -X GET -H "'Authorization: Bearer "' -H "'Content-Type: application/json"' https://management.azure.com/subscriptions//resourceGroups//providers/Microsoft.Resources/deployments/Microsoft.Databricks?api-version=2017-05-10 " bt sub rgsource
ret2=eval ris2
azr= ret2 | jq .
echo azr | jq .

name=azrproperties.parameters.workspaceName.value"]
id=az"]["id"]
loc=azrproperties.parameters.location.value"| tr -d '"'

rname= name.replace(".","-")
rg= rgsource| sed 's/\./-/g']

sku=azrproperties.parameters.tier.value"| tr -d '"'
if sku" = "Standard" : sku="standard" ;
if sku" = "Premium" : sku="premium" ;
fr.write('resource "' +  "' + '__' + "' {' tfp rg rname + '"\n')
fr.write('\t name = "' +  name + '"\n')
fr.write('\t resource_group_name = "' +  rgsource + '"\n')
fr.write('\t location = "' +  loc + '"\n')
fr.write('\t sku = "' +  sku + '"\n')
fr.write('}\n')
outid=azrproperties.outputResources[0]["id"]
cat outfile
statecomm=fr.write('terraform state rm . + '__' + " tfp rg rname
echo statecomm >> tf-staterm.sh
eval statecomm
#echo outid
evalcomm=fr.write('terraform import . + '__' +  " tfp rg rname outid
echo evalcomm >> tf-stateimp.sh
eval evalcomm


    ###############
    # specific code end
    ###############

    # tags block       
            try:
                mtags=azr[i]["tags"]
                fr.write('tags { \n')
                for key in mtags.keys():
                    tval=mtags[key]
                    fr.write('\t "' + key + '"="' + tval + '"\n')
                fr.write('}\n')
            except KeyError:
                pass

            fr.write('}\n') 
            fr.close()   # close .tf file

            if cde:
                with open(rfilename) as f: 
                    print f.read()

            tfrm.write('terraform state rm '+tfp+'.'+rg+'__'+rname + '\n')

            tfim.write('echo "importing ' + str(i) + ' of ' + str(count-1) + '"' + '\n')
            tfcomm='terraform import '+tfp+'.'+rg+'__'+rname+' '+id+'\n'
            tfim.write(tfcomm)  

        # end for i loop

        tfrm.close()
        tfim.close()
    #end stub