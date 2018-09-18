# include custom library into maven local repository:

mvn install:install-file -Dfile=../java-utils/base/target/base-0.1.jar -DgroupId=com.google.code -DartifactId=base -Dversion=0.1 -Dpackaging=jar
mvn install:install-file -Dfile=../java-utils/sqljpa/target/sqljpa-0.1.jar -DgroupId=com.google.code -DartifactId=sqljpa -Dversion=0.1 -Dpackaging=jar


Reference:

http://www.mkyong.com/maven/how-to-include-library-manully-into-maven-local-repository/