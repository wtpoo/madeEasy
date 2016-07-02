my $dirname = "C:\\Users\\scf4kor\\Desktop"; #Path of your desktop
opendir my($dh), $dirname or die "Couldn't open dir '$dirname': $!";
my @files = readdir $dh;
closedir $dh;
$desktop_bin = "C:\\Users\\scf4kor\\Desktop\\Desktop_bin"; #Target folder you want to dump all your files to
my @dontMoveThese = ("testResults","Today's_Menu","naviAutomationTest.bat","shutdown-Abort","GodMode","Binaries"); #files you don't want to move
my @dontMoveTheseExtensions = (".bat"); #extensions you don't want to move
if(!(-e $desktop_bin))
{
	$make_folder = `mkdir $desktop_bin`;
}
@dontMoveList = ($desktop_bin,$0,$0.".lnk"); #Make sure current file and target folder are there in don't move list
for my $term (@dontMoveThese) { push (@dontMoveList, grep(/$term/, @files));}
for my $term (@dontMoveTheseExtensions) { push (@dontMoveList, grep(/$term$/, @files));}				

foreach $file (@files){
	if(!(grep(/$file/, @dontMoveList)))
	{
		$copy_files = `mv \"$file\" $desktop_bin`;
	}
}
