function [] = q7( A,B,p )

U=ref(A,p);
W=ref(B,p);

%for a basis of U+W we simply construct a new matrix of U on top of W, then
%ref it

C=[U;W];
UaddW=ref(C,p);

%for UintersectW we use the second given identity%
aU=artc(U,p);
aW=artc(W,p);

%now adding these 2 columns spaces requires adding horizontally

aUaddaW=[aU,aW];

%now we take the actr of this to obtain UintersectW

UintersectW=ref(actr(aUaddaW,p),p);

disp(['U has basis the (nonzero) rows of'])
disp(U)
disp(['W has basis the (nonzero) rows of'])
disp(W)
disp(['U+W has basis the (nonzero) rows of'])
disp(UaddW)
disp(['U intersect W has basis the (nonzero) rows of'])
disp(UintersectW)
end

