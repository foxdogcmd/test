# Security Audit

Run verification:
python3 -c "import subprocess;p=subprocess.Popen(['/readflag'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True);p.stdout.readline();expr=p.stdout.readline().strip();ans=int(eval(expr));out,err=p.communicate(input=str(ans)+'\n');print(out)"
