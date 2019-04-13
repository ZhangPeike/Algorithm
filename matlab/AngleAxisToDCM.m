function dcm = AngleAxisToDCM(vec, theta)
%   dcm=eye(3)
  c=cos(theta)
  v=1-c  
  s=sin(theta)
  x=vec(1)
  y=vec(2)
  z=vec(3)
  dcm=[x*x*v+c x*y*v-z*s x*z*v+y*s;
      x*y*v+z*s x*y*v+c y*z*v-x*s;
      x*z*v-y*s y*z*v+x*s z*z*v+c]
end
