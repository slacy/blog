Title: KVM won't boot Ubuntu with module installed (on Intel)
Date: 2008-03-16 08:52
Author: slacy
Category: General
Tags: install, kvm, ubuntu, xen
Status: published

So, I'm planning on using [KVM](http://kvm.qumranet.com/kvmwiki) to
virtualize my new server, but when I try to boot any of the install ISO
images, I get a message like this:

> \# kvm -no-acpi -vnc :1 -m 2000 -cdrom ./ubuntu-7.10-jeos-i386.iso
> ../test.img -boot d  
> exception 6 (0)  
> rax 0000000000000469 rbx 0000000000800001 rcx 0000000000004300 rdx
> 0000000000000000  
> rsi 000000000005961d rdi 000000000005961c rsp 00000000fffaa9cc rbp
> 000000000000200c  
> r8 0000000000000000 r9 0000000000000000 r10 0000000000000000 r11
> 0000000000000000  
> r12 0000000000000000 r13 0000000000000000 r14 0000000000000000 r15
> 0000000000000000  
> rip 000000000000b04b rflags 00033006  
> cs 4143 (00041430/0000ffff p 1 dpl 3 db 0 s 1 type 3 l 0 g 0 avl 0)  
> ds 4004 (00040040/0000ffff p 1 dpl 3 db 0 s 1 type 3 l 0 g 0 avl 0)  
> es 4004 (00040040/0000ffff p 1 dpl 3 db 0 s 1 type 3 l 0 g 0 avl 0)  
> ss 0000 (00000000/0000ffff p 1 dpl 3 db 0 s 1 type 3 l 0 g 0 avl 0)  
> fs 3002 (00030020/0000ffff p 1 dpl 3 db 0 s 1 type 3 l 0 g 0 avl 0)  
> gs 0000 (00000000/0000ffff p 1 dpl 3 db 0 s 1 type 3 l 0 g 0 avl 0)  
> tr 0000 (7d850000/00002088 p 1 dpl 0 db 0 s 0 type b l 0 g 0 avl 0)  
> ldt 0000 (00000000/0000ffff p 1 dpl 0 db 0 s 0 type 2 l 0 g 0 avl 0)  
> gdt 40920/47  
> idt 0/ffff  
> cr0 60000010 cr2 0 cr3 0 cr4 0 cr8 0 efer 0  
> code: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
> 00 00 00 00 00 00 00 00 00  
> Aborted

And, if I

> \# rmmod kvm kvm\_intel

Then it can boot, but without the KVM kernel modules, the performance is
horrible. [The KVM pages say that these exceptions are due to the fact
that some Intel processors doesn't emulate some 8088
instructions.](http://kvm.qumranet.com/kvmwiki/Intel_Real_Mode_Emulation_Problems?highlight=%28exception%29)
Well, if that means that I can't boot my install media, then its pretty
pointless, isn't it? BTW, would it be that hard to emulate these
unfrequently used instructions properly?

I'm going to see if I can get through the install process without the
kernel module (under full emulation), and then boot the resultant image
with the module installed, but I don't have much hope that it'll work
very well.

In the mean time, I'm reading up on Xen, which I think is a bit more
mature than KVM is...
