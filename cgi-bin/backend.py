#! /usr/bin/python3

import cgi
import subprocess as sp

print("content-type: text/html")
print()

req = cgi.FieldStorage()
ch = req.getvalue("ch")

pod_name = req.getvalue("pname")
deploy_name = req.getvalue("dname")
port = req.getvalue("port")
image = req.getvalue("image")
replica_no = req.getvalue("rno")
output="" 

# create deployment

if (("create" in ch)or("deploy" in ch)or("launch" in ch)or("run" in ch)) and (("deployment" in ch)or("deployments" in ch)):
 
    output = sp.getoutput("sudo kubectl create deployment {} --image={} --kubeconfig admin.conf" .format(deploy_name,image))

# create pod 

elif if (("create" in ch)or("launch" in ch)or("run" in ch)) and (("pod" in ch)or("pods" in ch)):
   
    output = sp.getoutput("sudo kubectl run {} --image={} --kubeconfig admin.conf".format(pod_name,image))

# show deployments

elif (("show" in ch))or("display" in ch)or("get" in ch))and(("deployment" in ch)or("deployments" in ch)):
   
    output = sp.getoutput("sudo kubectl get deployments --kubeconfig admin.conf")

# show pods

elif (("show" in ch)or("display" in ch)or("get" in ch))and(("pods"in ch)or("pod" in ch)):
   
    output = sp.getoutput("sudo kubectl get pod --kubeconfig admin.conf")

# expose service 

elif (("expose"in ch))and(("deployment" in ch)or("deployments" in ch)):
   
    output = sp.getoutput("sudo kubectl expose deployment {} --type=NodePort --port={} --kubeconfig admin.conf" .format(deploy_name,port))

# scale replica 

elif (("scale"in ch))and(("replica"in ch)):
   
    output = sp.getoutput("sudo kubectl scale deployment {} --replicas={} --kubeconfig admin.conf".format(deploy_name,replica_no))

# delete deployment 

elif (("destroy" in ch)or(("remove" in ch)or("delete"in ch))and(("deployment"in ch)or("deployments" in ch)):
   
    output = sp.getoutput("sudo kubectl delete deployment {} --kubeconfig admin.conf".format(deploy_name))

# delete pod 

elif (("destroy" in ch)or(("remove" in ch)or("delete"in ch))and(("pod"in ch)):
   
    output = sp.getoutput("sudo kubectl delete pod {} --kubeconfig admin.conf".format(pod_name))

# delete entire environment 

elif (("destroy" in ch)or(("remove" in ch)or("delete"in ch))and(("env" in ch)or("envirnoment" in ch)or("deployments" in ch)):
   
   output = sp.getoutput("sudo kubectl delete all --all --kubeconfig admin.conf")

else:
   output = "enter correct requirements!!!"
print("""<style>
   body{
       background-color: black;
      text-align:center;
       justify-content:center;
     }
      pre{
        font-size: 40px;
        color:DC143C;
      font-weight: bold;
      padding -top:0px
}
h1{
color : red;
padding-bottom:0px;
}
</style>""")
print("""
<body>


<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRFWK8Y9uu0NshXAB-ieGzw2M0Q73uO9zV7FA&usqp=CAU" alt="kubernetes" height = "200px" class="center">
<pre>
<h1 style = "">🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆</h1>
{}
<h1 style = "">🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆</h1>
</pre>
</body>
""".format(output))
